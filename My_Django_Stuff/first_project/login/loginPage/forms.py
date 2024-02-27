from django import forms

class FormLogin(forms.Form):
    userId = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(),max_length=20)

class RegisterAccount(forms.Form):
    userId = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    age = forms.CharField(max_length=20)
    dob = forms.CharField(max_length=20)