from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name,self.phone,self.email,self.date_created


class Product(models.Model):
    CATEGORY = (('Indoor', 'Indoor'),('Out Door', 'Out Door'),)   
    name= models.CharField(max_length=200, null=True)
    price= models.FloatField(null=True)
    category= models.CharField(max_length=200, null=True,choices=CATEGORY)
    description= models.CharField(max_length=200, null=True)
    date_created= models.DateTimeField(auto_now_add=True,null=True)


class Order(models.Model):
    STATUS =(('Pending', 'Pending'),('Out for delivery', 'Out for delivery'),('Delivered', 'Delivered'),)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True,choices=STATUS)

