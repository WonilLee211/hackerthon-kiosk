from django.urls import path, include
from . import views

urlpatterns = [
    # menus
    path('menus/', views.menus, name='menus'),

    # burgers
    path('burgers/', views.burgers, name='burgers'),
    path('burger/<str:burger_name>/', views.burger_r, name='burger_r'),

    # beverages
    path('beverages/', views.beverages, name='beverages'),
    path('beverage/<str:beverage_name>/', views.beverage_r, name='beverage_r'),

    # side
    path('sides/', views.sides, name='sides'),
    path('side/<str:side_name>/', views.side_r, name='side_r'),
]
