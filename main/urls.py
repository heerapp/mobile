from django.urls import path
from . import views
from .views import product_list
from .views import CartDeleteView

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('video/', views.video, name="video"),
    path('<int:pk>/', views.product, name="product"),
    path('products/', views.all_product, name="all_products"),
    path('product/<slug>/', views.detail, name="detail"),
    path('add_product/', views.add_product, name="add_product"),
    path('add_category/', views.add_category, name="add_category"),
    path('api/', product_list),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.get_cart_items, name='cart'),
    path('remove-from-cart/<int:pk>/', CartDeleteView.as_view(), name='remove-from-cart'),
    path('ordered/', views.order_item, name='ordered'),
    path('order_details/', views.order_details, name='order_details'),

]
