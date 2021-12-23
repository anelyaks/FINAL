from .models import Articles
#  Product
from django.forms import ModelForm, TextInput, Textarea, NumberInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': "Your Name*",

            }),
            'email': TextInput(attrs={
                'placeholder': "Your Email*",

            }),
            'subject': TextInput(attrs={
                'placeholder': "Subject",

            }),
            'message': Textarea(attrs={
                'placeholder': "Message",
            })
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


