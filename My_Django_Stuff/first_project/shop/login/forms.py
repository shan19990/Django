from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    class Meta:
        model = User
        fields = ["username","email","password"]
