from django.db import models


# Create your models here.
class KjHotel(models.Model):
    email = models.EmailField(blank=True)
    mobile = models.BigIntegerField(blank=True)
    profile = models.FileField(default='media/default.jpg', upload_to='media/')
class details(models.Model):
    city = models.CharField(max_length=40,blank=True)
    hotel_name = models.CharField(max_length=50,blank=True)
    price = models.IntegerField(blank=True,default=5000)
    pic1 = models.ImageField(blank=True)
    pic2 = models.ImageField(blank=True,default='default.jpg')
    pic3 = models.ImageField(blank=True,default='default.jpg')
    pic4 = models.ImageField(blank=True,default='default.jpg')
    pic5 = models.ImageField(blank=True,default='default.jpg')
    pic6 = models.ImageField(blank=True,default='default.jpg')
class data(models.Model):
    email = models.EmailField(blank=True)
    hotel = models.CharField(max_length=50,blank=True)
    checkin = models.DateField()
    checkout = models.DateField()
    amount = models.IntegerField(blank=True)