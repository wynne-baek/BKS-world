from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('create/', views.review_create, name='review_create'),
    path('<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:review_pk>/comments/create/', views.review_comment_create, name='review_comment_create'),
    path('<int:review_pk>/like/', views.review_like, name='review_like'),
    path('<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('<int:review_pk>/update/', views.review_update, name='review_update'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.review_comment_delete, name='review_comment_delete'),
    #path('<int:review_pk>/comments/<int:comment_pk>/update/', views.review_comment_update, name='review_comment_update'),
]