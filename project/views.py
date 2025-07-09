from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


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


def get_post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_all.html', context={'posts': posts})


def post_info(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_info.html', context={'post': post})  


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user.is_superuser:
            post.delete()
    return redirect('posts_all')


def login_view(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
