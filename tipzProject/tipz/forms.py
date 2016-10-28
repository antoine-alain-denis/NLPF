from django.contrib.auth.models import User
from django import forms
from tipz.models import Pledge


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class PledgeForm(forms.ModelForm):

    class Meta:
        model = Pledge
        fields = ['title', 'description', 'value', 'project', 'investor']