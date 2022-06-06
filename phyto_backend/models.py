from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


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


# class Image(models.Model):
#     file = models.ImageField(upload_to="images")
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.update_at)
#
#
# class TaskHistory(models.Model):
#     class Status(models.TextChoices):
#         IN_PROGRESS = "IP", _('IN PROGRESS')
#         DONE = "D", _('DONE')
#         FAILED = "F", _('FAILED')
#
#     input_image = models.ForeignKey(Image, on_delete=models.CASCADE,
#                                     related_name="input_image")
#     output_image = models.ForeignKey(Image, on_delete=models.CASCADE,
#                                      related_name="output_image",
#                                      null=True,
#                                      blank=True)
#     created_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=2, choices=Status.choices,
#                               default=Status.IN_PROGRESS)
