from django.forms import ModelForm

from .models import PontuacaoQuiz,  post

class PostForm(ModelForm):
    class Meta:
        model = post
        fields = '__all__'
