from datetime import datetime
from django.core.management import BaseCommand

from Activity.models import UserDetail, ActivityPeriod


class Command(BaseCommand):
    """
  Add dummy data to user details
  """

    def handle(self, **options):
        self.add_dummy_user_details()

    @staticmethod
    def add_dummy_user_details():
        for i in range(0, 10):
            user_detail = UserDetail.objects.create(username='user'+str(i), first_name='user' + str(i), last_name='last_name' + str(i),
                                                    tz='America/Los_Angeles')
            for j in range(1, 3):
                ActivityPeriod.objects.create(user_detail=user_detail,
                                              start_time=datetime.strptime('Feb 1 2020  1:33PM', '%b %d %Y %I:%M%p'),
                                              end_time=datetime.strptime('Mar 1 2020  11:11AM', '%b %d %Y %I:%M%p'),
                                              )
