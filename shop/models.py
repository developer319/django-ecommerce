from math import degrees, trunc
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=64)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return f"{self.product_id} {self.product_name} {self.desc} "  



class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
        return f"{self.name} {self.email} {self.phone} {self.desc} "