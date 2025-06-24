from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Username')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Страница регистрации'
        db_table = 'project_registrations'

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Посты'
        db_table = 'project_posts'

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Категории'
        db_table = 'project_category'

    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя тега')
    
    class Meta:
        verbose_name_plural = 'Теги'
        db_table = 'project_tags'

    def __str__(self):
        return self.name

