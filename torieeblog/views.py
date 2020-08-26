from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost
from .serializers import BlogpostSerializer

# Create your views here.


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by("-date_created")
    serializer_class = BlogpostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by("-date_created")
    serializer_class = BlogpostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogpostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostCategoryView(ListAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        category = data["category"]
        queryset = BlogPost.objects.order_by(
            "-date_created").filter(category__iexact=category)

        serializer = BlogpostSerializer(queryset, many=True)

        return Response(serializer.data)
