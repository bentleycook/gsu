from django.db import models


class Person(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)
