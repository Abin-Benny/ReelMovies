from django.shortcuts import render,redirect
from .models import details,reviews
from django.contrib import messages
from .forms import ReviewForm
from django.core.exceptions import ObjectDoesNotExist

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
        movies = details.objects.all().order_by('Category__category_name')
    return render(request,"index.html",{'movies':movies})


def movie_details(request,movie_slug):
    try:
        movies = details.objects.get(slug=movie_slug)
        userreview = reviews.objects.filter(movie_id=movies.id)
    except Exception as e:
        raise e
    context={'movies': movies,'userreview':userreview}
    return render(request, "movie_details.html",context)

def user_reviews(request,movies_id):
    url = request.META.get('HTTP_REFERER')
    if request.method=='POST':
        try:
            ureview = reviews.objects.get(movie__id=movies_id,user__id=request.user.id)
            form = ReviewForm(request.POST,instance=ureview)#If the logined user already post a review,instance=ureview given in ReviewForm update the current review
            form.save()
            messages.success(request,'Your review has been updated')
            return redirect(url)
        except ObjectDoesNotExist:
            form = ReviewForm(request.POST)#If the logined user did not post any review,use this code
            if form.is_valid():
                data = reviews()
                data.title = form.cleaned_data['title']
                data.movie_id = movies_id
                data.user_id = request.user.id
                data.review = form.cleaned_data['review']
                data.rating = form.cleaned_data['rating']
                data.ip = request.META.get('REMOTE_ADDR')
                data.save()
                messages.success(request, 'Your review has been submitted')
                return redirect(url)





