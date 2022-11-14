from django.urls import path
from restapi import views

urlpatterns = [
    path('videos/', views.VideoList.as_view(), name='video-list'),
    path('videos/<int:pk>/', views.VideoDetail.as_view(), name='video-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('categories/<int:pk>/videos/', views.CategoryVideoDetail.as_view(), name='category-video-detail'),
]
