from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    publish_date = models.DateTimeField()
    tags = TaggableManager()
