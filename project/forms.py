from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Имя пользователя'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label='Email'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label='Введите пароль'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label='Подтвердите пароль'
    )