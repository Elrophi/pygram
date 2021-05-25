from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    image_name = models.TextField()
    description = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')


class Comment(models.Model):
    post = models.ForeignKey(Image, on_delete=models.CASCADE)
    text = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
