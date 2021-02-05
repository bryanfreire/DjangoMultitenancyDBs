from django.db import models


class Realm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField('auth.user', related_name='realms')

    def __str__(self):
        return self.name
