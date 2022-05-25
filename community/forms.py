from django import forms
from .models import Review, Comment

RATE_CHOICE = [tuple([x, x]) for x in range(1, 6)]

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ('title', 'movie_title', 'rate', 'content')
        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control my-2', 'rows': 1, 'style': 'width: 300px;'}),
            'movie_title': forms.Textarea(attrs={'class': 'form-control my-2', 'rows': 1, 'style': 'width: 300px;'}),
            'rate': forms.Select(choices=RATE_CHOICE),
            'content': forms.Textarea(attrs={'class': 'form-control my-2', 'style': 'width: 750px;', 'rows': 10})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control my-2 mx-auto', 'style': 'min-width: 680px; max-width: 1100px;', 'rows': 3})
        }
