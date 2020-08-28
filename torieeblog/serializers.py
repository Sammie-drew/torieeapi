from rest_framework import serializers
from .models import BlogPost, Genres


class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
        lockupfield = "slug"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = "__all__"
