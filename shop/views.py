import random
from builtins import id

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

from .models import Event, Category, CartItem, ShopCart
from .forms import SignUpForm


def home(request, category_slug=None, subcategory_slug=None):
    if all((category_slug is not None, subcategory_slug is not None)):
        events = Event.objects.filter(subcategory__slug=subcategory_slug)
    elif category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        events = Event.objects.filter(subcategory__category=category_page)
    else:
        events = Event.objects.all()

    random_events = list(events)
    random.shuffle(random_events)

    return render(request, 'shop/index.html', {'events': random_events})


def event_detail(request, category_slug, subcategory_slug, event_slug):
    event = Event.objects.get(subcategory__slug=subcategory_slug,
                              slug=event_slug)
    return render(request, 'shop/event.html', {'event': event})


def signUp(request):
    print(request.method)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
        print(form.is_valid())

    return render(request, 'shop/signup.html', {'form': form})


def signIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})


def signOut(request):
    logout(request)
    return redirect('login')


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, event_id):
    event = Event.objects.get(id=event_id)
    try:
        cart = ShopCart.objects.get(cart_id=_cart_id(request))
    except ShopCart.DoesNotExist:
        cart = ShopCart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(event=event, shop_cart=cart)
        if cart_item.quantity < cart_item.event.quantity:
            cart_item.quantity += 1
            cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(event=event, quantity=1,
                                            shop_cart=cart)
        cart_item.save()

    return redirect('cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = ShopCart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(shop_cart=cart, active=True)
        for cart_item in cart_items:
            total += cart_item.event.event_cost * cart_item.quantity
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'shop/cart.html', {'cart_items': cart_items,
                                              'total': total,
                                              'counter': counter})


def cart_remove(request, event_id):
    cart = ShopCart.objects.get(cart_id=_cart_id(request))
    event = get_object_or_404(Event, id=event_id)
    cart_item = CartItem.objects.get(event=event, shop_cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_detail')


def cart_remove_product(request, event_id):
    cart = ShopCart.objects.get(cart_id=_cart_id(request))
    event = get_object_or_404(Event, id=event_id)
    cart_item = CartItem.objects.get(event=event, shop_cart=cart)
    cart_item.delete()

    return redirect('cart_detail')
