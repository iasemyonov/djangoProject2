from .models import task
from django.forms import ModelForm, TextInput


class taskform(ModelForm):
    class Meta:
        model= task
        fields= ["title","task"]
        widgets={
            "title": TextInput(attrs={

                'class':'form-control',
                'placeholder': "url"
            }),
            "task": TextInput(attrs={

                    'class': 'form-control',
                    'placeholder': "opisanie"
                }),

        }
