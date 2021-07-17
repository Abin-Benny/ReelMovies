from django.db import models
from category.models import category
from genre.models import genre
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class details(models.Model):
    movie_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.CharField(max_length=5000)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    cast = models.CharField(max_length=1000)
    year_release = models.CharField(max_length=20)
    time = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')
    Category = models.ForeignKey(category,on_delete=models.CASCADE)
    Genre = models.ForeignKey(genre,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.movie_name)

    def get_url(self):
        return reverse('movie_details', args=[self.slug])

class reviews(models.Model):
    movie = models.ForeignKey(details, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250,blank=True)
    review = models.TextField(max_length=500,blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=250,blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)