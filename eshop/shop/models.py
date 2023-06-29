from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    # assuming one-to-one relationship between User and shippingaddress
    shipping_address = models.OneToOneField('ShippingAddress', on_delete=models.CASCADE, null=True, blank=True)
    # assuming one-to-many relationship between user and order
    orders = models.ManyToManyField('Order', related_name='users', blank=True)

    def __str__(self):
        return self.username


class ShippingAddress(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # assuming many-to-many relationship between cart and product
    products = models.ManyToManyField('Product', related_name='carts')
    sum = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Cart for {self.user}"


class Order(models.Model):
    sum = models.DecimalField(max_digits=8, decimal_places=2)
    # assuming one-to-many relationship between order and cart
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # additional order details

    def __str__(self):
        return f"Order {self.id}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name
