from django.shortcuts import render, redirect, get_object_or_404


def review_list(request):
    return render(request, 'community/reviewlist.html')

def review_create(request):
    pass

def review_detail(request):
    return render(request, 'community/reviewdetail.html')

def comment_create(request):
    pass