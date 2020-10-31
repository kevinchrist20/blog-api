from rest_framework import serializers
from .models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "uuid", "title", "category", "author", "content", "images", "created_at"]
