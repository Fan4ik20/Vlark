from .models import Category, ShopCart, CartItem

from .views import _cart_id


def menu_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = ShopCart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(shop_cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except ShopCart.DoesNotExist:
            item_count = 0

    return {'item_count': item_count}

