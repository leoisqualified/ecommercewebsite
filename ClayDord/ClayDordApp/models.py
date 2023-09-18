from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=20, null= True)
	email = models.EmailField(max_length=254, null= True)
 
class Products(models.Model):
    name = models.CharField(max_length=50, null= True)
    price = models.FloatField()
    description = models.CharField(max_length=254, null= True)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null= True)

class Order(models.Model):
    STATUS =(
		('pending','pending'),
		('out for delivery','out for delivery'),
		('delivered','delivered')
	)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null= True, choices=STATUS)