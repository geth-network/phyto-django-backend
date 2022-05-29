from .models import UserHistory
from rest_framework import serializers


class ImageDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserHistory
        exclude = ['result', 'time_update']
