from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_home, name='movie_home'),
    path('list/', views.movie_search, name='movie_search'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),

]