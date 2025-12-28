from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from .models import CustomUser


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = CustomUser.CUSTOMER
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = RegisterUserForm()
    return render(request, "accounts/register_user.html", {"form": form})
