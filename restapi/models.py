from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
