from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib import messages
from hashlib import sha256
<<<<<<< HEAD
from django.contrib.auth import authenticate, login
=======
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
>>>>>>> accounts
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

<<<<<<< HEAD
'''def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request,"login.html")'''
=======
def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
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


def user_logout(request):
    logout(request)
    return redirect("login")
>>>>>>> accounts


