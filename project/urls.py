from django.urls import path

from .views import post_info, get_post_list, delete_post, post_update, create_post


urlpatterns = [
    path('posts/<int:id>/', post_info, name='post_info'),
    path('posts/', get_post_list, name='posts_all'),
    path('post/<int:id>/delete/', delete_post, name='delete_post'),
    path('posts/<int:id>/update/', post_update, name='post_update'),
    path('posts/add/', create_post, name='create_post')
]