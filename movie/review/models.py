from django.db import models
from category.models import category
from genre.models import genre

# Create your models here.
class details(models.Model):
    movie_name = models.CharField(max_length=250)
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

