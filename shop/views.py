from django.shortcuts import render

# Create your views here.

from .models import Event


def home(request):
    events = Event.objects
    return render(request, 'shop/index.html', {"events": events})


def ticket_detail(request):
    return render(request, 'shop/ticket_detail.html')

