import uuid
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from timezone_field import TimeZoneField


# Create your models here.


class UserDetail(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tz = TimeZoneField()


class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_detail = models.ForeignKey(
        "UserDetail", related_name="UserGroup", on_delete=models.CASCADE
    )
