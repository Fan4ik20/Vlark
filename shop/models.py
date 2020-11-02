from django.db import models


# Create your models here.


class Region(models.Model):
    region_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.region_name


class City(models.Model):
    city_name = models.CharField(max_length=40)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name


class Event(models.Model):
    event_name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    event_date = models.DateTimeField()
    event_cost = models.FloatField(default=0)
    event_address = models.CharField(max_length=50)
    event_img = models.ImageField(upload_to="event_img/")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class User(models.Model):
    nickname = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50, unique=True)


class ShopCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)


class OrderDetail(models.Model):
    quantity = models.DecimalField(max_digits=2, decimal_places=0)
    price = models.FloatField(default=0)
    shop_cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
