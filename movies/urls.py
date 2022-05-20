from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_home, name='movie_home'),
    path('list/', views.search_movie, name='search_movie'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),

]