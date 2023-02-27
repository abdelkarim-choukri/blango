from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from blog.api.serializers import PostSerializer, UserSerializer
from blog.models import Post
from rest_framework.permissions import IsAdminUser
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blango_auth.models import User


class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]


class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer