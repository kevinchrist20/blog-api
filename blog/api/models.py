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
    content = models.TextField()
    date_create = models.DateTimeField(default=timezone.now)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING)
    updated_at = models.DateTimeField(auto_now=True)
