from .models import Category, Subcategory


def menu_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}
