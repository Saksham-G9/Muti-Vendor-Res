from django import forms
from accounts.models import CustomUser
from .models import Vendor


class VendorForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )
    vendor_license = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "btn"})
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "password",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter Last Name"}),
            "username": forms.TextInput(attrs={"placeholder": "Enter Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter Email"}),
            "phone_number": forms.TextInput(
                attrs={"placeholder": "Enter Phone Number"}
            ),
        }
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "username": "Username",
            "email": "Email Address",
            "phone_number": "Phone Number",
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data
