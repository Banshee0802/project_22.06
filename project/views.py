from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm


def get_post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_all.html', context={'posts': posts})


def post_info(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_info.html', context={'post': post})  

@login_required
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