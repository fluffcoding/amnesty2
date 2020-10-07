
from blog.models import Category



def all_categories_context(request):
    universal_categories = Category.objects.all()
    context = {
        'universal_categories': universal_categories,
    }
    return context