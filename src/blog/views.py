from django.shortcuts import render
from .models import Post



def post_view(request):
    return render(request, 'blog/post.html', {})


def latest(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/latest.html', context)