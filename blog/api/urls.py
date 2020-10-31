from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.Categories.as_view(), name="categories"),
    path("categories/<int:pk>/", views.CategoryDetail.as_view(), name="category")
]

urlpatterns = format_suffix_patterns(urlpatterns)
