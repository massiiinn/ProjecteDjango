from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    path('posts/', views.posts, name='posts'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('authors/', views.authors_list, name='authors'),
    path('authors/<int:pk>/', views.author_detail, name='author-detail'),
    path('tags/', views.tags_list, name='tags'),
    path('tags/<int:tag_id>/', views.tag_detail, name='tag-posts'),
]
