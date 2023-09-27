from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE, null = True, blank = True)
	name = models.CharField(max_length=20, null= True)
	email = models.EmailField(max_length=254, null= True)
 
class Product(models.Model):
    name = models.CharField(max_length=50, null= True)
    price = models.FloatField()
    #image
    description = models.TextField(max_length=254, null= True)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null= True)

class Order(models.Model):
    STATUS =(
		('pending','pending'),
		('out for delivery','out for delivery'),
		('delivered','delivered')
	)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null= True, choices=STATUS)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False, null = True, blank = False)
    transaction_id = models.CharField(max_length = 200, null = True)

class OrderItem(models.Model):
	product = models.ForeignKey(Product,on_delete=models.SET_NULL, null= True)
	quantity = models.IntegerField(default = 0, null = True)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL, null= True)
	date_added = models.DateTimeField(auto_now_add = True)

class ShippingAddress(models.Model):
	customer = models.OneToOneField(Customer, on_delete =models.SET_NULL, blank = True, null = True)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL, null= True)
	city = models.CharField(max_length=20, null= True)
	state = models.CharField(max_length=20, null= True)
	zipcode = models.CharField(max_length=20, null= True)
	date_added = models.DateTimeField(auto_now_add = True)