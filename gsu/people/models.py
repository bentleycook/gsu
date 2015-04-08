from django.db import models

from jsonfield import JSONField


class Person(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    personal_data = JSONField()
