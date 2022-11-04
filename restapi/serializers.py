from dataclasses import fields
from rest_framework import serializers
from restapi.models import Video, Category


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'category']


class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = ['id', 'title', 'color']
