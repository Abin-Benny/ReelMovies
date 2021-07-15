from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib import messages
from hashlib import sha256
from django.contrib.auth import authenticate, login
# Create your views here.



def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)
        user = authenticate(request,username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("index")
    return render(request,"login.html")


