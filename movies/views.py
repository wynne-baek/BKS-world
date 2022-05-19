from django.shortcuts import render, redirect, get_object_or_404


def movie_home(request):
    return render(request, 'movies/moviehome.html')

def movie_list(request):
    return render(request, 'movies/movielist.html')

def movie_detail(request):
    return render(request, 'movies/moviedetail.html')


