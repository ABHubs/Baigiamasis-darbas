from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    shipping_address = models.OneToOneField('ShippingAddress', on_delete=models.CASCADE, null=True, blank=True)
    orders = models.ManyToManyField('Order', related_name='users', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class ShippingAddress(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"

    class Meta:
        verbose_name = _('shipping_address')
        verbose_name_plural = _('shipping_addresses')


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', related_name='carts')
    sum = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Cart for {self.user}"

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')


class Order(models.Model):
    sum = models.DecimalField(max_digits=8, decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id}"

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

