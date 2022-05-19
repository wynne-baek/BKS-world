from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST, require_http_methods

from .forms import CustomUserCreationForm

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:movie_home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('movies:movie_home')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:movie_home')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:movie_home')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('movies:movie_home')

@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        # 팔로우 받는 사람과 request_user
        you = get_object_or_404(get_user_model(), pk=user_pk)
        me = request.user

        # 나 자신은 팔로우 할 수 없다.
        if you != me:
            # 이미 팔로우 한 상태에서 누르면 언팔로우
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                followed = False
            else:
                # 팔로우
                you.followers.add(me)
                followed = True

            follow_status = {
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
                'followed': followed,
            }
            return JsonResponse(follow_status)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')