from django.db import models

# Create your models here.
from django.db import models

class Industry(models.Model):
    name = models.CharField(max_length=200)
    electricity_consumption = models.FloatField()
    fuel_consumption = models.FloatField()
    waste_production = models.FloatField()
    employee_count = models.IntegerField()
    production_volume = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Household(models.Model):
    address = models.CharField(max_length=200)
    electricity_consumption = models.FloatField()
    gas_consumption = models.FloatField()
    vehicle_count = models.IntegerField()
    resident_count = models.IntegerField()
    waste_production = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)