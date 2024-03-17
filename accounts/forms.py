from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile

"""
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'nazwa użytkownika', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'hasło', 'class': 'form-control'}))
"""


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'nazwa użytkownika', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'adres email', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': '<PASSWORD>', 'class': 'form-control'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są takie same')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nazwa_firmy', 'adres', 'kod_pocztowy', 'miasto', 'NIP', 'telefon')
