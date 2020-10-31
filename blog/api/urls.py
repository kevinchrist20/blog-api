from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.Categories.as_view(), name="categories"),
    path("categories/<int:pk>/", views.CategoryDetail.as_view(), name="category"),
    path("post/", views.create_post, name="create_post"),
    path("post_detail/<int:pk>", views.post_detail, name="post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
