from random import randint, choice
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Url(models.Model):
    __tablename__ = 'urls'

    def __str__(self):
        return self.url

    def _random_user():
        #pseude random workaround for order_by('?') slowness
        count = User.objects.all().count()
        if not count:
            return None
        while True:
            try:
                random_index = randint(0, count - 1)
                return User.objects.get(pk=random_index)
            except User.DoesNotExist:
                pass

    def _url_id():
        CHAR_SET = string.ascii_uppercase + string.digits + string.ascii_lowercase

        while True:
            length = randint(*settings.SHORT_URL_LENGTH_BOUNDS)
            short_id = ''.join(choice(CHAR_SET) for x in range(length))
            try:
                temp = Url.objects.get(pk=short_id)
            except Url.DoesNotExist:
                return short_id

    short_id = models.SlugField(primary_key=True, default=_url_id)
    url = models.URLField(max_length=2000, unique=True)
    counter = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    submitter = models.ForeignKey(User, default=_random_user)
