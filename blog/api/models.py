import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Blog(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.models.TextField()
    date_create = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING)
    date_updated = models.DateTimeField(auto_now=True)
