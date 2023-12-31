from django import forms
from Moviesapp.models import Moviesapp

class filmform(forms.ModelForm):
    class Meta:
        model=Moviesapp
        fields="__all__"