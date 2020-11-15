import random

from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Event, Category, Subcategory


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
