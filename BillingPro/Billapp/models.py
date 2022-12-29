from django.db import models

# Create your models here.
class Billing(models.Model):
    bilNo = models.IntegerField()
    customerName = models.CharField(max_length=20)
    dateTime = models.DateTimeField(auto_now_add=True)
    mobileNo = models.IntegerField()
    amountValue = models.FloatField()


class EstimatedBill(models.Model):
    bilNo = models.IntegerField()
    customerName = models.CharField(max_length=20)
    dateTime = models.DateTimeField(auto_now_add=True)
    mobileNo = models.IntegerField()
    estimatedValue = models.FloatField()

class CombinedBilling(models.Model):
    bilNo = models.IntegerField()
    customerName = models.CharField(max_length=20)
    dateTime = models.DateTimeField(auto_now_add=True)
    mobileNo = models.IntegerField()
    amountValue = models.FloatField()
    estimatedValue = models.FloatField()