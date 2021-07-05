from django.db import models

# Create your models here.
class register(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=250)
    Phone = models.CharField(max_length=20)


    def __str__(self):
        return self.First_name

