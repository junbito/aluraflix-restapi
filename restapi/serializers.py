from restapi.models import Video, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class VideoSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.all(), required=False)
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'category_id', 'owner']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'color']


class CategoryVideoSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['videos']


class UserSerializer(serializers.ModelSerializer):
    videos = serializers.PrimaryKeyRelatedField(many=True, queryset=Video.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'videos']
