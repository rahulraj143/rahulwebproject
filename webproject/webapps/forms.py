from django import forms
from .models import webapps
class MovieForm(forms.ModelForm):
    class Meta:
                model=webapps
                fields=['name','desc','year','img']
