from django import forms
from .models import Todo
from django.contrib.admin import widgets


class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['title', 'details']
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control data-field'}),
            "details": forms.Textarea(attrs={'class': 'form-control data-field', 'cols': '20', 'row': '5', 'style': 'height: 90px;'}),
        }



