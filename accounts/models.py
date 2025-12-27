from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUserManager(BaseUserManager):
    def create_user(
        self, first_name, last_name, username, email, password=None, **extra_fields
    ):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")

        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, first_name, last_name, username, email, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            first_name, last_name, username, email, password, **extra_fields
        )


class CustomUser(AbstractBaseUser):
    RESTAURANT = 1
    CUSTOMER = 2
    USER_TYPE_CHOICES = (
        (RESTAURANT, "Restaurant"),
        (CUSTOMER, "Customer"),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=CUSTOMER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="users/profile_pictures/", blank=True, null=True
    )
    cover_photo = models.ImageField(
        upload_to="users/cover_photos/", blank=True, null=True
    )
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    pin_code = models.CharField(max_length=10, blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    def full_address(self):
        return f"{self.address}, {self.city}, {self.state}, {self.country} - {self.pin_code}"