from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('<int:id>/', views.movie_detail, name='movie-detail'),
    path('populate/', views.populate_movies, name='populate_movies'),
    path('debug-genres/', views.debug_movie_genres)
]