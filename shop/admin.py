from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Region)
admin.site.register(models.City)
admin.site.register(models.Event)
admin.site.register(models.Category)
admin.site.register(models.Subcategory)
admin.site.register(models.User)
admin.site.register(models.ShopCart)
admin.site.register(models.OrderDetail)
admin.site.register(models.Ticket)
admin.site.register(models.PaymentMethod)


