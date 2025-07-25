from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import PostForm


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


def create_post(request):
    title = "Создать пост"
    submit_button_text = 'Создать'

    if request.method == 'GET':
        form = PostForm()

        return render(request, 'posts/post_form.html', context={'form': form, 'title': title, 'submit_button_text': submit_button_text})
    
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()

            return redirect('post_info', id=post.id)
        else:
            return render(request, 'posts/post_form.html', context={'form': form, 'title': title, 'submit_button_text': submit_button_text})


def post_update(request, id):
    title = 'Редактировать пост'
    submit_button_text = 'Обновить'
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            updated_post = form.save()
            return redirect('post_info', id=updated_post.id)
    else:
        return render(request, 'posts/post_form.html', context={'form': form, 'title': title, 'submit_button_text': submit_button_text})

    form = PostForm(instance=post)
    
    return render(request, 'posts/post_form.html', context={'form': form, 'title': title, 'submit_button_text': submit_button_text})


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()

        return redirect('posts_all')
    
    return render(request, 'posts/post_delete.html', {'post': post})