from django.contrib import admin

# Register your models here.
from Activity.models import ActivityPeriod, UserDetail

admin.site.register(UserDetail)
admin.site.register(ActivityPeriod)