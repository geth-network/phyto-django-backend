from django.contrib.auth.forms import AuthenticationForm, UsernameField, \
    UserCreationForm
from django import forms

from .models import User


class UserAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'placeholder': 'имя пользователя'}),
        label=''
    )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'placeholder': 'пароль'}),
    )


class UserRegistrationForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'placeholder': 'имя пользователя'}),
        label='Имя пользователя'
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'ваше имя'}),
        label='Ваше имя'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'ваша фамилия'}),
        label='Ваша фамилия'
    )
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'placeholder': 'пароль'}),
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'placeholder': 'подтвердите пароль'}),
        strip=False,
    )
    field_order = ['username', 'first_name', 'last_name', 'password1',
                   'password2']

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
