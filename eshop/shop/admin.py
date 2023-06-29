from django.contrib import admin
from .models import User, ShippingAddress, Cart, Order, Product

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'sum')
    list_filter = ('user__username',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('cart', 'sum')
    list_filter = ('cart__user__username',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name',)

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'postal_code', 'country', 'phone_number')
    list_filter = ('city', 'state', 'country')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_filter = ('username',)

admin.site.register(User, UserAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)

