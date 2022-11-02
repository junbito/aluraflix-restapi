from restapi.models import Video
from restapi.serializers import VideoSerializer
from rest_framework import generics


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
