from rest_framework import serializers
from restapi.models import Video, Category


class VideoSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.all(), required=False)
    
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'category_id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'color']

class CategoryVideoSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['videos']
