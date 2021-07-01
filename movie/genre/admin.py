from django.contrib import admin
from .models import genre

# Register your models here.
class genreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('genre_name',)}
    list_display = ('genre_name','slug')

admin.site.register(genre, genreAdmin)
