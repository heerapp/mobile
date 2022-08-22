from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('slug', 'status', 'latest',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('slug',)
