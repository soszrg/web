from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    
class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    
