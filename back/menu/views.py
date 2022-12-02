from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import BurgerSerializer, BeverageSerializer, SidedishSerializer
from .models import Burger, Sidedish, Beverage
from rest_framework import status
from rest_framework.response import Response


# Create your views here.


def makeDB(request):
    burgerNames = ["더블_비프_미트_칠리_버거", "맥크리스피_클래식_버거", "미트_칠리_BLT버거", "빅맥"]
    burgerprices = [7500, 5600, 7000, 4900]
    sideNames = ["골든모짜렐라_치즈스틱", "아이스크림콘", "초코콘", "후렌치후라이"]
    sideprices = [1000, 900, 1000, 1700]
    beverNames = ["아이스바닐라_라떼", "카페라떼", "코카콜라_제로", "코카콜라"]
    beverprices = [3200, 3200, 2600, 2600]

    for i in range(4):
        burgerdict = dict()
        sidedict = dict()
        beverdict = dict()
        
        burgerdict['name'] = burgerNames[i]
        burgerdict['image'] = f'media/burgers/{burgerNames[i]}.png'
        burgerdict['price'] = burgerprices[i]
        burgerSerializer = BurgerSerializer(data=burgerdict)
        burgerSerializer.is_valid()
        burgerSerializer.save()

        sidedict['name'] = sideNames[i]
        sidedict['image'] = f'media/sides/{sideNames[i]}.png'
        sidedict['price'] = sideprices[i]
        sideSerializer = SidedishSerializer(data=sidedict)
        sideSerializer.is_valid()
        sideSerializer.save()

        beverdict['name'] = beverNames[i]
        beverdict['image'] = f'media/bever/{beverNames[i]}.png'
        beverdict['price'] = beverprices[i]
        beverageSerializer = BeverageSerializer(data=beverdict)
        beverageSerializer.is_valid()
        beverageSerializer.save()
        
        

@api_view(['GET'])
def burgers(request):
    _burgers = Burger.objects.all()
    serializer = BurgerSerializer(_burgers, many=True)
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
    serializer = BeverageSerializer(_beverages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def beverage_r(request, beverage_name):
    _beverage = get_object_or_404(Beverage, name=beverage_name)
    serializer = BurgerSerializer(data=_beverage)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def sides(request):
    _sidedish = Sidedish.objects.all()
    serializer = SidedishSerializer(_sidedish, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def side_r(request, side_name):
    _side = get_object_or_404(Sidedish, name=side_name)
    serializer = BurgerSerializer(data=_side)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)
