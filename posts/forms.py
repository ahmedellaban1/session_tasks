from django.forms import ModelForm
from .models import Post


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['auther', 'title', 'content', 'publish_date', 'tags', 'image',]
