from django.db import models
from taggit.managers import TaggableManager

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
#     usr = models.CharField()
    
class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    pwd = models.CharField(max_length=20)
    
class BlogInfo(models.Model):
    blog_id = models.IntegerField()
    tags = TaggableManager()
    
