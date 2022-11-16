from restapi.models import Video, Category
from restapi.serializers import VideoSerializer, CategorySerializer, CategoryVideoSerializer, UserSerializer
from restapi.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User


class VideoList(generics.ListCreateAPIView):
    """
    List all videos, or create a new video.
    """
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        """
        Optionally restricts the returned videos of a given category,
        by filtering against a `search` query parameter in the URL.
        """
        queryset = Video.objects.all()
        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(title=search)
        return queryset


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a video.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response("Video successfully deleted.")


class CategoryList(generics.ListCreateAPIView):
    """
    List all categories, or create a new category.
    """    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response("Category successfully deleted.")


class CategoryVideoDetail(generics.RetrieveAPIView):
    """
    Retrieve the videos of a category.
    """    
    queryset = Category.objects.all()
    serializer_class = CategoryVideoSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserList(generics.ListAPIView):
    """
    List all users.
    """    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
