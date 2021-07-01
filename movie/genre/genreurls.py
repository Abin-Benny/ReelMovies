from django.urls import path
from . import views

urlpatterns=[
    path('<slug:genre_slug>/', views.index_by_genre, name="index_by_genre"),
    ]