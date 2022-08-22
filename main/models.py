from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from embed_video.backends import detect_backend


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=100)
    video = EmbedVideoField()

    class Meta:
        verbose_name_plural = "Video"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="mobile")
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to="media", blank=True)
    detail = models.TextField(max_length=300)
    status = models.CharField(max_length=30, blank=True)
    latest = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CartItems(models.Model):
    ORDER_STATUS = (
        ('Active', 'Active'),
        ('Delivered', 'Delivered')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    ordered_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Active')
    delivery_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def __str__(self):
        return self.product.name




