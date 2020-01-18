from django.db import models

# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=300, unique=True)
    url = models.URLField(max_length=300, unique=True)
    tags = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
