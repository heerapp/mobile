from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        result = Product.objects.filter(name__icontains=query)
        return render(request, 'base.html', {'product': result})
    content = {
        "categories": categories,
        "products": products,
    }
    return render(request, 'main/home.html', content)


@permission_required('is_superuser', raise_exception=True)
def dashboard(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    video = Video.objects.all()
    content = {
        "categories": categories,
        "products": products,
        "video": video,
    }
    return render(request, 'main/dashboard.html', content)


def product(request, pk):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=pk)
    content = {
        "categories": categories,
        "products": products,
    }
    return render(request, 'main/product.html', content)


def all_product(request):
    products = Product.objects.all()
    return render(request, 'main/product.html', {"products": products})


def detail(request, slug):
    products = Product.objects.filter(name=slug)
    return render(request, 'main/product.html', {"products": products})


@permission_required('is_superuser', raise_exception=True)
def add_product(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        product= form.save(commit=False)
        product.save()
        return redirect('/dashboard')
    return render(request, 'main/add_product.html', {'form': form})


@permission_required('is_superuser', raise_exception=True)
def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        category = form.save(commit=False)
        category.save()
        return redirect('/dashboard')
    return render(request, 'main/add_category.html', {'form': form})


@api_view(['GET'])
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@login_required(login_url='login')
def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    cart_item = CartItems.objects.create(
        product=product,
        user=request.user,
        ordered=False,
    )
    messages.info(request, "Added to Cart!!Continue Shopping!!")
    return redirect("main:cart")


@login_required(login_url='login')
def get_cart_items(request):
    cart_items = CartItems.objects.filter(user=request.user, ordered=False)
    bill = cart_items.aggregate(Sum('product__price'))
    total = bill.get("product__price__sum")
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'main/cart.html', context)


class CartDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CartItems
    success_url = '/cart'

    def test_func(self):
        cart = self.get_object()
        if self.request.user == cart.user:
            return True
        return False


@login_required(login_url='login')
def order_item(request):
    cart_items = CartItems.objects.filter(user=request.user, ordered=False)
    ordered_date = timezone.now()
    cart_items.update(ordered=True, ordered_date=ordered_date)
    return redirect("main:order_details")


@login_required(login_url='login')
def order_details(request):
    items = CartItems.objects.filter(user=request.user, ordered=True, status="Active").order_by('-ordered_date')
    cart_items = CartItems.objects.filter(user=request.user, ordered=True, status="Delivered").order_by('-ordered_date')
    bill = items.aggregate(Sum('product__price'))
    number = items.aggregate(Sum('quantity'))
    total = bill.get("product__price__sum")
    count = number.get("quantity__sum")
    context = {
        'items': items,
        'cart_items': cart_items,
        'total': total,
        'count': count,
    }
    return render(request, 'main/order_details.html', context)


def video(request):
    video = Video.objects.all()
    return render(request, 'main/video.html', {'video': video})



