from urllib.parse import urlencode
from urllib.request import urlopen
import datetime
import json

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import get_current_timezone


FAKE_USERS_URL = 'https://randomuser.me/api/'

class Command(BaseCommand):
    help = 'Fetch [user_no] users from randomuser.me and creates them in the DB'

    def add_arguments(self, parser):
        parser.add_argument('user_no', nargs='+', type=int)

    def handle(self, *args, **options):
        tz = get_current_timezone()
        date_format = '%Y-%m-%d %H:%M:%S'
        user_no = options['user_no'][0]

        urlargs = urlencode({
            'results': user_no,
            'inc': ','.join(['name', 'login', 'email', 'registered'])
        })

        users_data = urlopen(FAKE_USERS_URL+'?'+urlargs).read()
        users = json.loads(users_data.decode('utf-8'))['results']

        for user in users:
            date_object = tz.localize(
                datetime.datetime.strptime(user['registered'], date_format)
            )

            new_user = User(
                username=user['login']['username'],
                first_name=user['name']['first'],
                last_name=user['name']['last'],
                email=user['email'],
                password=user['login']['password'],
                date_joined=date_object
            )
            new_user.save()