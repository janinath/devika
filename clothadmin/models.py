from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.TextField(max_length=50,db_column='name',null=True)   

    def __str__(self) :
        return self.name
class Product(models.Model):
    title=models.TextField(max_length=50,db_column='name',null=True)
    description=models.TextField(max_length=50,db_column='description',null=True)
    price=models.PositiveIntegerField(db_column='price',null=True)
    image=models.ImageField(upload_to='dresses',db_column='image',null=True)
    category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    def __str__(self) :
        return self.title
    
class Staff(models.Model):
  
    name=models.TextField(max_length=50,db_column='name',null=True)
    staffid=models.TextField(max_length=50,db_column='description',null=True)
    password=models.TextField(max_length=50,db_column='price',null=True)
    
    def __str__(self) :
        return self.name
    
