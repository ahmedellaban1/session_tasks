from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm


# Create your views here.
def add_post(request, *args, **kwargs):
    form = AddPostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/all-posts')
    form = AddPostForm()
    context = {
        'page_title': 'add new post',
        'form': form
    }
    return render(request, 'add_new_post.html', context)


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

# TODO: add edit_post, delete_post, class based view, over ride template-name
# TODO: all pages redirect to all-post
# TODO: search discuss
