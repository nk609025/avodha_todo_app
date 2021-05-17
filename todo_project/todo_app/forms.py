from django import forms
from . models import Task

class Todoforms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']