from django.shortcuts import render

# Create your views here.

from .models import Event, Ticket


def home(request, category_slug=None):
    events = Event.objects
    return render(request, 'shop/index.html', {"events": events})


def event_detail(request, category_slug, subcategory_slug, event_slug):
    event = Event.objects.get(subcategory__slug=subcategory_slug,
                              slug=event_slug)
    return render(request, 'shop/event.html', {'event': event})

