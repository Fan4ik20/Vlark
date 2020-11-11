from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ticket/', views.ticket_detail, name='ticket_detail')

]