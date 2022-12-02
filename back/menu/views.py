from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from back.menu.models import Burger, Beverage, Sidedish
from back.menu.serializers import BurgerSerializer, BeverageSerializer


# Create your views here.

@api_view(['GET'])
def burgers(request):
    _burgers = Burger.objects.all()
    serializer = BurgerSerializer(data=_burgers, many=True)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def burger_r(request, burger_name):
    _burger = get_object_or_404(Burger, name=burger_name)
    serializer = BurgerSerializer(data=_burger)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def beverages(request):
    _beverages = Beverage.objects.all()
    serializer = BeverageSerializer(data=_beverages, many=True)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def beverage_r(request, beverage_name):
    _beverage = get_object_or_404(Beverage, name=beverage_name)
    serializer = BurgerSerializer(data=_beverage)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def sides(request):
    _sides = Sidedish.objects.all()
    serializer = BeverageSerializer(data=_sides, many=True)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def side_r(request, side_name):
    _side = get_object_or_404(Sidedish, name=side_name)
    serializer = BurgerSerializer(data=_side)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)
