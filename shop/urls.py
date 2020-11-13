from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>/<slug:subcategory_slug>/<slug:event_slug>/',
         views.event_detail, name='event_detail')
]

