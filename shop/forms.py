from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=40, help_text='eg@mail.com')
    birth_date = forms.DateField(help_text='m/d/y')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1',
                  'password2', 'email', 'birth_date',)
