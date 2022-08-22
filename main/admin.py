from django.contrib import admin
from .models import Category, Product, CartItems, Video

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItems)
admin.site.register(Video)
