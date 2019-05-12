from django.contrib import admin
from .models import UserProfile, Member

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Member)
