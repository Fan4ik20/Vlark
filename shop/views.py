import random

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

from .models import Event, Category, Subcategory
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
