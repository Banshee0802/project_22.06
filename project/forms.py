from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Максимальная длина 200 символов'}),
            'text': forms.Textarea(attrs={
                'class': "form-control",
                'rows': 5,
        })
        }
        labels = {
            'title': 'Заголовок поста',
            'text': 'Текст поста'
        }
    