from django.urls import path, include
from . import views

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('order/<int:order_id>/', views.order_r, name='order_r'),
    path('order/<int:order_id>/', views.order_c, name='order_c'),
    path('order/<int:order_id>/', views.order_d, name='order_d'),
]
