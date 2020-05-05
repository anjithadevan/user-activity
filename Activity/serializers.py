from rest_framework import serializers

from Activity.models import UserDetail, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ("start_time", "end_time")


class UserDetailsSerializer(serializers.ModelSerializer):
    tz = serializers.CharField(required=False)
    real_name = serializers.SerializerMethodField()
    activity_periods = ActivityPeriodSerializer(source="UserGroup", many=True)

    class Meta:
        model = UserDetail
        fields = ("id", "real_name", "tz", "activity_periods")

    def get_real_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)


