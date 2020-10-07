from django.shortcuts import render, get_object_or_404
from .models import Post


def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)


def latest(request):
    posts = Post.objects.all()
    total = len(posts)
    context = {
        'posts': posts,
        'total': total,
    }
    return render(request, 'blog/latest.html', context)


def category(request, id):
    filtered_posts = Post.objects.filter(category=id)
    print(filtered_posts)
    total = len(filtered_posts)
    context = {
        'posts': filtered_posts,
        'total': total,
    }
    return render(request, 'blog/latest.html', context)