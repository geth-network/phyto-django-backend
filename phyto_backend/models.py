from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return self.username


class UserHistory(models.Model):
    image = models.ImageField(upload_to="input-images")
    result = models.ImageField(null=True, blank=True,
                               upload_to="result-images")
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.time_update)