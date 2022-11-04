from django.urls import path
from restapi import views

urlpatterns = [
    path('videos', views.VideoList.as_view()),
    path('videos/', views.VideoList.as_view()),
    path('videos/<int:pk>', views.VideoDetail.as_view()),
    path('videos/<int:pk>/', views.VideoDetail.as_view()),
    path('categories', views.CategoryList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>', views.CategoryDetail.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]
