from django.shortcuts import render,redirect
from review.models import details
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=='POST':
        mname = request.POST.get('searchname')
        movies = details.objects.filter( movie_name=mname)
        if movies.count()==0:
            movies = details.objects.all()
            messages.info(request, "Requested movie is not available.")
            return render(request, "index.html", {'movies':movies})
    else:
        movies = details.objects.all()
    return render(request,"index.html",{'movies':movies})

