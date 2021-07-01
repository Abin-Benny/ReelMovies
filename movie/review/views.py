from django.shortcuts import render,redirect
from review.models import details

# Create your views here.
def index(request):
    movies = details.objects.all()
    return render(request,"index.html",{'movies':movies})

