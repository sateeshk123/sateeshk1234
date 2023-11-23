from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    userid=models.CharField(max_length=40,primary_key=True)
    uname=models.CharField(max_length=50)
    pwd=models.CharField(max_length=20)
    phone=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=12,null=True)
    isadmin=models.BooleanField(default=False)
    createdon=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table="users"
        ordering=['-createdon']

class Event(models.Model):
    eventid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=40,null=True)    
    maxcapacity=models.IntegerField()
    photo=models.ImageField(upload_to='pics',default='noimage.png')
    createdon=models.DateTimeField(auto_now=True)
    isavailable=models.BooleanField(default=True)

    class Meta:
        db_table="events"
        ordering=['-eventid']


class FoodItem(models.Model):
    fid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    unit=models.CharField(max_length=20)
    remarks=models.CharField(max_length=50,null=True)

    class Meta:
        db_table="fooditems"
        ordering=['-fid']   

class Booking(models.Model):
    bid=models.AutoField(primary_key=True)
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    book_date=models.DateField()
    event=models.ForeignKey(to=Event,on_delete=models.CASCADE)
    status=models.CharField(max_length=30,default='Pending')
    userstatus=models.CharField(max_length=20,null=True)
    createdon=models.DateTimeField(auto_now=True)
    adults=models.IntegerField(default=0)
    child=models.IntegerField(default=0)
    
    cardno=models.CharField(max_length=16,null=True)
    amount=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    progress=models.DecimalField(max_digits=5,decimal_places=2,null=True)

    class Meta:
        db_table="bookings"
        ordering=["-bid"]

class BookingItem(models.Model):
    itemid=models.AutoField(primary_key=True)
    item=models.ForeignKey(to=FoodItem,on_delete=models.CASCADE)
    booking=models.ForeignKey(to=Booking,on_delete=models.CASCADE)
    qty=models.IntegerField()

    class Meta:
        db_table="bookingitems"
