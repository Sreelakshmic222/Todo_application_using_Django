from django import forms
from .models import Register,Login

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Register
        fields ='__all__'
class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
        password = forms.CharField(widget=forms.PasswordInput)