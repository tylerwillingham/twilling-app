from rest_framework.views import APIView
from blog.models import Post, Status, Category
from blog.serializers import PostSerializer, StatusSerializer, CategorySerializer
from rest_framework.response import Response


class PostList(APIView):
    """
    List all Posts
    """
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class StatusList(APIView):
    """
    List all statuses
    """
    def get(self, request, format=None):
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data)


class CategoryList(APIView):
    """
    List all categories
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
