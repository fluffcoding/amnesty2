from django.shortcuts import render
from django.db.models import Q

from blog.models import Post, Category



def index(request):
    context = {

    }
    return render(request, 'main/index.html', context)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        'query': query,
        'posts': queryset,
        'results_number': len(queryset)
    }

    print(queryset)
    return render(request, 'main/search_results.html', context)