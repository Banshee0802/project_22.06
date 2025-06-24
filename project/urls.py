from django.urls import path

from .views import home_view

from . import views

urlpatterns = [
    path('', home_view),
    path('profile/', views.profile, name='profile'),
    path('content/', views.content, name='content'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]