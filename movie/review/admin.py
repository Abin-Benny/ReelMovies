from django.contrib import admin
from .models import details
# Register your models here.
class detailsAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'director','Category')

admin.site.register(details,detailsAdmin)