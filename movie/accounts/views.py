from django.shortcuts import render
from accounts.forms import registerform
# Create your views here.



def register(request):
    form = registerform()
    return render(request,"register.html",{'form':form})

def login(request):
    return render(request,"login.html")

def logout(request):
    return