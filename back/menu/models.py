from django.db import models


# Create your models here.


class Burger(models.Model):
    name = models.TextField()
    price = models.IntegerField()


class Beverage(models.Model):
    name = models.TextField()
    price = models.IntegerField()


class Side(models.Model):
    name = models.TextField()
    price = models.IntegerField()
