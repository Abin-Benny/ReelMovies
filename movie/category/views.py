from django.shortcuts import render,redirect,get_object_or_404
from review.models import details
from category.models import category


# Create your views here.
def index(request,category_slug=None):

    if category_slug!=None:
        categories = get_object_or_404(category,slug=category_slug)
        movies = details.objects.filter(Category=categories)
        return render(request, "index.html", {'movies': movies})
    else:
        return redirect("index")
