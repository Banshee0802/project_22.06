from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('Главная страница')

def profile(request):
    return HttpResponse('Профиль пользователя')

def content(request):
    return HttpResponse('Контент')

def contact(request):
    return HttpResponse('Контакты')

def about(request):
    return HttpResponse('О нас')
