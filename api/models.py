from django.db import models
from enum import Enum

class RoleChoice(Enum):  
    ow = "Owner"
    Hi = "Hirer"
    Ad = "Admin"
class user(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    role = models.CharField(
      max_length=20,
    #   choices=[(tag, tag.value) for tag in RoleChoice]  
    )

    def __str__(self):
            return self.username
    
    class Meta:
        db_table = "user"

class car(models.Model):
 
    carid = models.AutoField(primary_key=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE)
    carmake = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    price = models.IntegerField()
    insurance=models.CharField(max_length=50)
    rcbook=models.CharField(max_length=50)
    ismanual=models.BooleanField()
    kmsdriven=models.IntegerField()
    numofseats=models.IntegerField()
    ispetrol=models.BooleanField()
    mileage=models.IntegerField()
    
    class Meta:
        db_table = "car"

    # def __str__(self):
    #     return self.carid,self.carmake,self.carmodel

class booking(models.Model):
    bookingid = models.AutoField(primary_key=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE)
    carid=models.ForeignKey(car,on_delete=models.CASCADE)
    startdate=models.DateTimeField()
    returndate=models.DateTimeField()
    extratime=models.DateTimeField()
    totalprice=models.IntegerField()
    ismanual=models.BooleanField()

    class Meta:
        db_table = "booking"

    # def __str__(self):
    #     return self.bookingid

class rating(models.Model):
    bookingid=models.ForeignKey(booking,on_delete=models.CASCADE)
    userid=models.ForeignKey(user,on_delete=models.CASCADE)
    rating=models.IntegerField()

    class Meta:
        db_table = "rating"

class manual_pickup(models.Model):
    bookingid=models.ForeignKey(booking,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    pickupdate=models.DateField()

    class Meta:
        db_table = "manual_pickup"
    
class doorstep_pickup(models.Model):
    bookingid=models.ForeignKey(booking,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    deliverydate=models.DateField()
    cost=models.IntegerField()

    class Meta:
        db_table = "doorstep_pickup"

class payment(models.Model):
    bookingid=models.ForeignKey(booking,on_delete=models.CASCADE)
    advanceamount=models.IntegerField()
    paymentdate=models.DateTimeField()
    paymenttype=models.CharField(max_length=50)
    totalamount=models.IntegerField()
    remamount=models.IntegerField()
    class Meta:
        db_table = "payment"

class complaints(models.Model):
    bookingid=models.ForeignKey(booking,on_delete=models.CASCADE)
    fromuser=models.ForeignKey(user,on_delete=models.CASCADE,related_name='fromuser')
    touser=models.ForeignKey(user,on_delete=models.CASCADE,related_name='touser')
    complaintmessage=models.CharField(max_length=250)
    complaintdate=models.DateField()
    class Meta:
        db_table = "complaints"

class cancellation(models.Model):
    bookingid=models.ForeignKey(booking,on_delete=models.CASCADE)
    cancelreason=models.CharField(max_length=250)
    canceldate=models.DateField()
    cancellationfee=models.IntegerField()
    refundamount=models.IntegerField()
    class Meta:
        db_table = "cancellation"

class license(models.Model):
    userid=models.ForeignKey(user,on_delete=models.CASCADE)
    license=models.CharField(max_length=250)
    class Meta:
        db_table = "license"