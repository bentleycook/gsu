
from django.db import models
from django.utils.timezone import now

from people.models import Person


class Talk(models.Model):

    title = models.CharField(max_length=300)
    speaker = models.ForeignKey(Person)
    datetime = models.DateTimeField()

    def time_until_start(self):
        return self.datetime - now()
