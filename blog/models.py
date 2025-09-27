from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    auther = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title