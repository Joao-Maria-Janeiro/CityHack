from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from nodes.models import Day, Division

User = get_user_model()

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=100)
    monthly_waste = models.FloatField(default=-1.0)
    divisions = models.ManyToManyField(Division, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_waste = models.FloatField(default=-1.0)
    monthly_waste = models.FloatField(default=-1.0)
    monthly_budget = models.FloatField(default=-1.0)
    current_day = models.IntegerField(default=-1)
    current_month = models.IntegerField(default=-1)
    # electricity_costs = (
    #     ('1.15', 0.1595),
    #     ('2.3', 0.1598),
    #     ('3.45', 0.15690),
    #     ('4.6', 0.16050),
    #     ('5.75', 0.16170),
    #     ('6.9', 0.16190),
    #     ('10,35', 0.16200),
    #     ('13,8', 0.16330),
    #     ('17,25', 0.16420),
    # )
    # energy_plan = models.FloatField(choices=electricity_costs, default='5.75')
    energy_plan = models.FloatField(default=-1.0)
    days = models.ManyToManyField(Day, blank=True)
    divisions = models.ManyToManyField(Division, blank=True)
    members = models.ManyToManyField(Member, blank=True)

    def __str__(self):
        return self.user.username


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
