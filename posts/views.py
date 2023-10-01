from django.shortcuts import render
from .models import Post


# Create your views here.
def posts_list(request, *args, **kwargs):
    queryset = Post.objects.all()
    context = {
        "page_title": "all posts",
        "posts": queryset,
    }
    return render(request, 'all-posts.html', context)


def post_details(request, *args, **kwargs):
    post = Post.objects.get(id=kwargs['id'])
    context = {
        "page_title": f"post {post.id} details",
        "post": post,
    }
    return render(request, 'post-details.html', context)
