from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('<slug:movie_slug>/', views.movie_details, name="movie_details"),
    #path('<slug:category_slug>/',views.index,name="index_by_category"),

    ]