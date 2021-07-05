from django import forms
from accounts.models import register


class registerform(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'