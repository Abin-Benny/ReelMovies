from django.shortcuts import render,redirect
from .models import details
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method=='POST':
        mname = request.POST.get('searchname')
        movies = details.objects.filter(movie_name=mname)
        if movies.count()==0:
            movies = details.objects.all()
            messages.info(request, "Requested movie is not available.")
            return render(request, "index.html", {'movies':movies})
    else:
        movies = details.objects.all()
    return render(request,"index.html",{'movies':movies})


def movie_details(request,movie_slug):
    try:
        movies = details.objects.get(slug=movie_slug)
    except Exception as e:
        raise e
    context={'movies': movies}
    return render(request, "movie_details.html",context)

