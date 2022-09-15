from django import forms
from .models import Users, MyAccountManager
from django.contrib.auth.forms import  AuthenticationForm


class RegesForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        

class LoginForm(AuthenticationForm):
  username = forms.EmailField(label='Email Address')