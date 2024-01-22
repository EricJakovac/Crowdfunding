from django.contrib import admin
from .models import UserProfile, Project, Donation, Support

model_list = [UserProfile, Project, Donation, Support]
admin.site.register(model_list)
