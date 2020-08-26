
from django.urls import path
from .views import (BlogPostListView, BlogPostCategoryView,
                    BlogPostFeaturedView, BlogPostDetailView)

urlpatterns = [
    path("", BlogPostListView.as_view(), name="bloglist"),
    path("featured/", BlogPostFeaturedView.as_view(), name="featured"),
    path("category/", BlogPostCategoryView.as_view(), name="blogcategory"),
    path("<slug>/", BlogPostDetailView.as_view(), name="blogdetails"),
]
