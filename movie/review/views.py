from django.shortcuts import render,redirect
from review.models import details

# Create your views here.
def index(request):
    if request.method=='POST':
        mname = request.POST.get('searchname')
        movies = details.objects.filter( movie_name=mname)
    else:
        movies = details.objects.all()
    return render(request,"index.html",{'movies':movies})

