from django.db import models

# Create your models here.
class Burger(models.Model):
    name = models.CharField(max_length=100)
    image = models.TextField(blank=True)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Sidedish(models.Model):
    name = models.CharField(max_length=100)
    image = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Beverage(models.Model):
    name = models.CharField(max_length=100)
    image = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    