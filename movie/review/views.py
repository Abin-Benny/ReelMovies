from django.shortcuts import render,redirect
from .models import details,reviews
from django.contrib import messages
from .forms import ReviewForm
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
    url = request.META.get('HTTP_REFERER')
    movies = details.objects.get(slug=movie_slug)
    print(movies)
    print(movies.id)
    if request.method == 'POST':
        try:
            ureview = reviews.objects.get(user__id=request.user.id,movie__id=movies.id)
            form = ReviewForm(request.POST,instance=ureview)  # If the logined user already post a review,instance=ureview given in ReviewForm update the current review
            form.save()
            return redirect(url)
        except reviews.DoesNotExist:
            form = ReviewForm(request.POST)  # If the logined user did not post any review,use this code
            if form.is_valid():
                data = reviews()
                data.title = form.cleaned_data['title']
                data.review = form.cleaned_data['review']
                data.rating = form.cleaned_data['rating']
                data.ip = request.META.get('REMOTE_ADDR')
                data.save()
                return redirect(url)

    form = ReviewForm(request.POST)
    context = {'movies': movies, 'form': form}
    return render(request, "movie_details.html", context)






'''def user_reviews(request,movies_id):
    url = request.META.get('HTTP_REFERER')
    if request.method=='POST':
        try:
            ureview = reviews.objects.get(user__id=request.user.id,movie__id=movies_id)
            form = ReviewForm(request.POST,instance=ureview)#If the logined user already post a review,instance=ureview given in ReviewForm update the current review
            form.save()
            return redirect(url)
        except reviews.DoesNotExist:
            form = ReviewForm(request.POST)#If the logined user did not post any review,use this code
            if form.is_valid():
                data = reviews()
                data.title = form.cleaned_data['title']
                data.review = form.cleaned_data['review']
                data.rating = form.cleaned_data['rating']
                data.ip = request.META.get('REMOTE_ADDR')
                data.save()
                return redirect(url)'''





