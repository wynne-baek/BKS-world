from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

@require_GET
def review_list(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/reviewlist.html', context)

@require_http_methods(['GET', 'POST'])
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:review_detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/reviewcreate.html', context)

@require_GET
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/reviewdetail.html', context)

@require_POST
def review_comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:review_detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/reviewdetail.html', context)

@require_POST
def review_like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            liked = False
        else:
            review.like_users.add(user)
            liked = True
        context = {
            'liked': liked,
            'count': review.like_users.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:login')

@require_POST
def review_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user.is_authenticated:
        if request.user == review.user:
            review.delete()
    return redirect('community:review_list')

@require_POST
def review_comment_delete(request, review_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('community:review_detail', review_pk)

@login_required
@require_http_methods(['GET', 'POST'])
def review_update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.user == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save()
                return redirect('community:review_detail', review.pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('community:review_list')
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'community/reviewupdate.html', context)

# @login_required
# @require_http_methods(['GET', 'POST'])
# def review_comment_update(request, comment_pk, review_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     form = CommentForm(instance=comment)
#     if request.method == "POST":
#         update_form = CommentForm(request.POST, instance=comment)
#         if update_form.is_valid():
#             update_form.save()
#             return redirect('community:review_detail', review_pk)
#     context = {
#         'comment': comment,
#         'form': form,
#     }
#     return render(request, 'community/reviewcommentupdate.html', context)



