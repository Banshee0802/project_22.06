from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Максимальная длина 200 символов'
            })
        }
        labels = {
            'title': 'Заголовок поста',
            'text': 'Текст поста'
        }
    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        
        if len(title) < 5:
            raise forms.ValidationError('Заголовок не должен быть короче 5 символов')

        return title