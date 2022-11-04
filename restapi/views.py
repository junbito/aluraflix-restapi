from restapi.models import Video, Category
from restapi.serializers import VideoSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.response import Response


class VideoList(generics.ListCreateAPIView):
    """
    List all videos, or create a new video.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a video.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response("Video successfully deleted.")


class CategoryList(generics.ListCreateAPIView):
    """
    List all categories, or create a new category.
    """    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response("Category successfully deleted.")
