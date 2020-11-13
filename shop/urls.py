from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.home,
         name='event_by_category'),
    path('category/<slug:category_slug>/subcategory/<slug:subcategory_slug>/',
         views.home,
         name='event_by_subcategory'),
    path('category/<slug:category_slug>/subcategory/<slug:subcategory_slug>/'
         '<slug:event_slug>/',
         views.event_detail, name='event_detail')
]
