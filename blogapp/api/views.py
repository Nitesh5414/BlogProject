from rest_framework.generics import (
                        ListAPIView, 
                        RetrieveAPIView, 
                        DestroyAPIView, 
                        UpdateAPIView, 
                        CreateAPIView)

from .serializers import (PostListSerializer, 
                          PostDetailSerializer,
                          PostCreateUpdateSerializer)
from blogapp.models import Post

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_queryset(self):
        return super().get_queryset()
    
class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

