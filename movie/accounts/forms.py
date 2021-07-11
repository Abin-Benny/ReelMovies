from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=50)


    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2','phone_number']

    def __init__(self,*args,**kwargs):
        super(UserForm,self). __init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'