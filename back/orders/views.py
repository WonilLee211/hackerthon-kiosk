from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def orders(request):
    pass


@api_view(['GET'])
def order_r(request, order_id):
    pass


@api_view(['POST'])
def order_c(request, order_id):
    pass


@api_view(['DELETE'])
def order_d(request, order_id):
    pass
