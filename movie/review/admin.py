from django.contrib import admin
from .models import details,reviews
# Register your models here.
class detailsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('movie_name',)}
    list_display = ('movie_name', 'director','Category')

admin.site.register(details,detailsAdmin)
admin.site.register(reviews)