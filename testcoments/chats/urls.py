from django.urls import path

from . import views

app_name = 'chats'
urlpatterns = [
    path('', views.all_comments, name='all_comments'),
    path('add_comment_to_post/', views.add_comment_to_post, name='add_comment_to_post'),
]
