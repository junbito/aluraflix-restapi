from dataclasses import fields
from rest_framework import serializers
from restapi.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url']
