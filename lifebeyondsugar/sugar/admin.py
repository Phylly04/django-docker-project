from django.contrib import admin
from .models import User, SugarIntake, HealthCondition

# Register your models here.
admin.site.register(User)
admin.site.register(SugarIntake)
admin.site.register(HealthCondition)
