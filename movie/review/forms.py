from django import forms
from .models import reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = reviews
        fields = ['title','review','rating']
