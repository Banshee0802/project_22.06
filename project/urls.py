from django.urls import path

from .views import home_view, post_info, get_post_list, delete_post, login_view, post_update

from . import views

urlpatterns = [
    path('', home_view),
    path('profile/', views.profile, name='profile'),
    path('content/', views.content, name='content'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('posts/<int:id>/', post_info, name='post_info'),
    path('posts/', get_post_list, name='posts_all'),
    path('post/<int:id>/delete/', delete_post, name='delete_post'),
    path('login/', login_view, name='login'), 
    path('posts/<int:id>/update/', post_update, name='post_update'),
]