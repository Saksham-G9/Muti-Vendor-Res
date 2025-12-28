from django import forms
from .models import CustomUser

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'role', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}),
            'role': forms.Select(choices=CustomUser.USER_TYPE_CHOICES, attrs={'class': 'chosen-select'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'role': 'Register As',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data
