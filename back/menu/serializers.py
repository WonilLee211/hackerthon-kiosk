from .models import Burger, Beverage, Sidedish

from rest_framework import serializers

class BurgerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Burger
        fields = '__all__'


class BeverageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beverage
        fields = '__all__'


class SidedishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sidedish
        fields = '__all__'
    
