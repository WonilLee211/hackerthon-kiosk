from django.db import models

# Create your models here.

class Order(models.Model):

    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return str(self.id)

class OrderItem(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) :
        return self.product