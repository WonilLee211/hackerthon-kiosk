from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def menus(request):
    pass


@api_view(['GET'])
def burgers(request):
    pass


@api_view(['GET'])
def burger_r(request, burger_name):
    pass


@api_view(['GET'])
def beverages(request):
    pass


@api_view(['GET'])
def beverage_r(request, beverage_name):
    pass


@api_view(['GET'])
def sides(request):
    pass


@api_view(['GET'])
def side_r(request, beverage_name):
    pass
