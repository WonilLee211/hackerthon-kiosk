from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order
from .serializers import OrderItemSerializer, OrderSerializer

burgerNames = ["더블_비프_미트_칠리_버거", "맥크리스피_클래식_버거", "미트_칠리_BLT버거", "빅맥"]
# burgerprices = [7500, 5600, 7000, 4900]
sideNames = ["골든모짜렐라_치즈스틱", "아이스크림콘", "초코콘", "후렌치후라이"]
# sideprices = [1000, 900, 1000, 1700]
beverNames = ["아이스바닐라_라떼", "카페라떼", "코카콜라_제로", "코카콜라"]
# beverprices = [3200, 3200, 2600, 2600]

# Create your views here.

@api_view(['GET'])
def orders(request):
    _orders = Order.objects.all()
    serializer = OrderSerializer(data=_orders, many=True)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def order_r(request, order_id):
    _order = get_object_or_404(Order, id=order_id)
    serializer = OrderSerializer(data=_order)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def order_c(request):
    order = Order()

    for order_item in request.data[orders]:
        serializer = OrderItemSerializer(data=order_item)

        if serializer.is_valid(raise_exception=True):
            serializer.save(order=order)

    return Response({"message": "OK"}, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def order_d(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    order.delete()
    return Response({"order_id": order_id}, status=status.HTTP_204_NO_CONTENT)
