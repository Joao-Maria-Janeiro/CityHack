from django.db import models

# Create your models here.
class Day(models.Model):
    day_number = models.IntegerField(default=-1)
    energy_per_day = models.FloatField(default=-1.0)

class DivionUser(models.Model):
    name = models.CharField(max_length=100)
    monthly_waste = models.FloatField(default=-1.0)

class Plug(models.Model):
    activation_key = models.CharField(max_length=100)
    current_monthly_waste = models.FloatField(default=-1.0)
    current_daily_waste = models.FloatField(default=-1.0)
    on = models.BooleanField(default = True)
    current_day = models.IntegerField(default=-1)
    name = models.CharField(max_length=100)

class Division(models.Model):
    users = models.ManyToManyField(DivionUser, blank=True)
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Plug, blank=True)
    daily_waste = models.FloatField(default=-1.0)
    monthly_waste = models.FloatField(default=-1.0)
    days = models.ManyToManyField(Day, blank=True)
