from random import randint, random
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from .models import Movie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def movie_home(request):
    num = randint(1, 5)
    context = {
        'num': num
    }
    return render(request, 'movies/moviehome.html', context)

def movie_search(request):
    # 검색 버튼을 눌렀을 때 실행,
    search = request.GET.get('search', '')
    if search:
        movies = Movie.objects.filter(country=f'{search}')
        paginator = Paginator(movies, 12)
        page_number = request.GET.get("page") 
        page_movies = paginator.get_page(page_number)
    else:
        movies = Movie.objects.all()
        paginator = Paginator(movies, 12)
        page_number = request.GET.get("page") 
        page_movies = paginator.get_page(page_number)
    # 1. 로그인 여부 확인
    # 2. 로그인 되어 있을 경우, 검색어 쿼리에 넣어서 해당 국가 정보가 들어있는 영화만 보여줌
    if request.user.is_authenticated:
        context = {
            'movies': page_movies,
        }
        return render(request, 'movies/movielist.html', context)
    # 1-2. 로그인 되어있지 않으면, 로그인 페이지로
    return redirect('accounts:login')

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all()
    context = {
        'movie': movie,
        'genres' : genres,
    }
    return render(request, 'movies/moviedetail.html', context)

