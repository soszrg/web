from django.db import models
from taggit.managers import TaggableManager

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    
class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    
class BlogInfo(models.Model):
    blog_id = models.IntegerField()
    tags = TaggableManager()
    
