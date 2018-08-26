from django.db import models

# Create your models here.

class Device(models.Model):
    android_id = models.CharField(max_length=200)
    serial_no = models.CharField(max_length=200)
    device_model = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    api_level = models.CharField(max_length=200)
    hardware = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)





