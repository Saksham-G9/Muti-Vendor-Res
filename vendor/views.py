from django.shortcuts import render, redirect
from django.views import View
from .forms import VendorForm
from .models import Vendor
from accounts.models import UserProfile, CustomUser


class RegisterVendorView(View):
    template_name = "vendor/register_vendor.html"
    form_class = VendorForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # Create the user
            user = form.save(commit=False)
            user.role = CustomUser.RESTAURANT
            user.set_password(form.cleaned_data["password"])
            user.save()

            user_profile = UserProfile.objects.create(user=user)

            Vendor.objects.create(
                user=user,
                user_profile=user_profile,
                vendor_license=form.cleaned_data["vendor_license"],
            )

            return redirect("login")

        return render(request, self.template_name, {"form": form})
