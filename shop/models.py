from django.db import models
from django.urls import reverse

# Create your models here.


class Region(models.Model):
    region_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.region_name

    class Meta:
        ordering = ('region_name',)
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'


class City(models.Model):
    city_name = models.CharField(max_length=40)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

    class Meta:
        ordering = ('city_name',)
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def get_url(self):
        return reverse('event_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250)

    def get_url(self):
        return reverse('event_by_subcategory',
                       args=[self.category.slug, self.slug])

    def __str__(self):
        return self.subcategory_name

    class Meta:
        ordering = ('category',)
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class Event(models.Model):
    event_name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    event_date = models.DateTimeField()
    event_cost = models.FloatField(default=0)
    event_address = models.CharField(max_length=50)
    event_img = models.ImageField(upload_to="event_img/")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True)

    def get_url(self):
        return reverse('event_detail', args=[self.subcategory.category.slug,
                                             self.subcategory.slug, self.slug])

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ('event_name',)


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


# class User(models.Model):
#     nickname = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=40)
#     email = models.CharField(max_length=40)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=50)
#     birth_date = models.DateField()


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50, unique=True)


class ShopCart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)


class CartItem(models.Model):
    # Maybe need to move field price from event to ticket???
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    shop_cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=2, decimal_places=0)
    active = models.BooleanField(default=True)
