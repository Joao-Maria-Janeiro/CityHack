from django.db import models

# Create your models here.
class NodeMCU(models.Model):
    activation_key = models.CharField(max_length=100)
    monthly_budget = models.FloatField(default=-1.0)
    current_daily_waste = models.FloatField(default=-1.0)
    current_monthly_waste = models.FloatField(default=-1.0)
    power = models.FloatField(default=-1.0)
    curr_day = models.IntegerField(default=-1)
    email = models.EmailField()
