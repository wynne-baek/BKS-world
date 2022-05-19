from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('create/', views.review_create, name='review_create'),
    path('<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:review_pk>/comments/create/', views.comment_create, name='comment_create'),
]