from django.db import models
import uuid
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Blog(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.models.TextField()
    date_create = models.DateTimeField(default=timezone.now)
    category = provider = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING)
    date_updated = models.DateTimeField(auto_now=True)
