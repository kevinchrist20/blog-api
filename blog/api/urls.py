from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_post, name="create_post"),
    path("post_detail/<int:pk>", views.post_detail, name="post_detail"),
]