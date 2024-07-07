from django.db import models

# Create your models here.
class Portfolio(models.Model):
    img=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=150)
    desc=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Service(models.Model):
    cus_name=models.CharField(max_length=150)
    cus_ph=models.CharField(max_length=12)
    cus_email=models.EmailField(max_length=50)
    name=models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.name



