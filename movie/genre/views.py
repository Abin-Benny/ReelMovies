from django.shortcuts import render,redirect,get_object_or_404
from review.models import details
from genre.models import genre


# Create your views here.
def index_by_genre(request,genre_slug=None):
    if genre_slug != None:
        genres = get_object_or_404(genre, slug=genre_slug)
        movies = details.objects.filter(Genre=genres)
        return render(request, "index.html", {'movies': movies})
    else:
        return redirect("index")
