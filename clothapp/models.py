from django.db import models
from clothadmin.models import Product

# Create your models here.
class Customer(models.Model):
    name=models.TextField(db_column="name",null=True)
    dob=models.TextField(db_column="dob",null=True)
    mob=models.TextField(db_column="mob",null=True)
    state=models.TextField(db_column="state",null=True)
    address=models.TextField(db_column="address",null=True)
    pincode=models.TextField(db_column="pincode",null=True)
    landmark=models.TextField(db_column="landmark",null=True)
    email=models.TextField(db_column="email",null=True)
    password=models.TextField(db_column="password",null=True)
   

    class Meta:
        db_table="customer"

class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)

class Contactus(models.Model):
    name=models.TextField(max_length=200,db_column='name',null=True)
    email=models.TextField(max_length=200,db_column='email',null=True)
    message=models.TextField(max_length=200,db_column='message',null=True)
    def __str__(self):
        return self.name