from .models import genre

def menu_links(request):
    genre_links = genre.objects.all()
    return dict(genre_links=genre_links)
