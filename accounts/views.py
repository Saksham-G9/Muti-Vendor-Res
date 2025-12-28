
from django.shortcuts import render, redirect
from .forms import RegisterUserForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Optionally, you can log the user in or redirect to login page
            return redirect('login')  # Change to your login url name
    else:
        form = RegisterUserForm()
    return render(request, 'accounts/register_user.html', {'form': form})