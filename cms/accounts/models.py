from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(null=True,blank = True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Dor','Out Dor')
    )
    name        = models.CharField(max_length=200)
    price       = models.FloatField()
    category    = models.CharField(max_length=200,null = True, choices= CATEGORY)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out For Delivery','Out For Delivery'),
        ('Delivery', 'Delivery')
    )
    customer =  models.ForeignKey(Customer,null=True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length = 200,null= True, choices = STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name
