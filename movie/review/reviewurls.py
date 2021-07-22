from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('<slug:movie_slug>/', views.movie_details, name="movie_details"),
    path('User_Reviews/<int:movies_id>', views.user_reviews, name="user_reviews"),
    ]