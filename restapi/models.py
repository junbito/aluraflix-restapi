from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    category = models.ForeignKey('Category', related_name='videos', default=1, on_delete=models.SET_DEFAULT)
    owner = models.ForeignKey('auth.User', related_name='videos', on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
