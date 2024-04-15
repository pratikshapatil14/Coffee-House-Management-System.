from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class coffee(models.Model):
    CAT=(1,'COLD COFFEE'),(2,'HOT COFFEE'),(3,'BLACK COFFEE'),(4,'COFFEE HOUSE SPECIAL')
    name=models.CharField(max_length=50)
    price=models.FloatField()
    cdetails=models.CharField(max_length=1000)
    cat=models.IntegerField()
    is_active=models.BooleanField(default=True)
    cimage=models.ImageField(upload_to='image')

    # def _str_(self):
    #     return self.name

class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    cid=models.ForeignKey(coffee,on_delete=models.CASCADE,db_column="cid")
    qty=models.IntegerField(default=1)

class Order(models.Model):
    Order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    cid=models.ForeignKey(coffee,on_delete=models.CASCADE,db_column="cid")
    qty=models.IntegerField(default=1)

class booktable(models.Model):
    userid=models.IntegerField()
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phoneno=models.BigIntegerField()
    date=models.DateField()
    time=models.TimeField()
    people=models.IntegerField()
    message=models.CharField(max_length=1000)
    status=models.CharField(max_length=1000,default="request submited")
   
