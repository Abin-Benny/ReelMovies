from django.db import models
from django.urls import reverse

# Create your models here.
class genre(models.Model):
    genre_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=255,blank=True)
    genre_image = models.ImageField(upload_to='categories',blank=True)

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def get_url(self):
        return reverse('index_by_genre', args=[self.slug])

    def __str__(self):
        return self.genre_name