from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Category, Blog
from .serializers import PostSerializer, CategorySerializer


# Create your views here.
@csrf_exempt
def index(req):
    """
    List all post
    """
    posts = Blog.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)
