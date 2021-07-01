from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    #path('<slug:genre_slug>/', views.index_by_genre, name="index_by_genre"),
    #path('<slug:category_slug>/',views.index,name="index_by_category"),

    ]