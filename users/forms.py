from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.forms import StyleForMixin
from users.models import User


class UserRegisterForm(StyleForMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleForMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
