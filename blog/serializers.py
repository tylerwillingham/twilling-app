from rest_framework import serializers
from blog.models import Post, Status, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title','slug', 'status', 'categories', 'body', 'created_at', 'updated_at')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'title', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')