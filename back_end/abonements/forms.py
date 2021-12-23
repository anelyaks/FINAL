from django.forms import ModelForm, TextInput

from .models import  buy


class buy(ModelForm):
    class Meta:
        model = buy
        fields = ['name', 'number']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': "Your Name*",

            }),
            'number': TextInput(attrs={
                'placeholder': "Your number*",

            })
        }
