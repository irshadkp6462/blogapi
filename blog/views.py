from django.shortcuts import render

# Create your views here.
from blog.serializers import UserCreationSerializer,PostSerializer

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from blog.models import Post

from rest_framework import authentication,permissions




class UsercreationView(CreateAPIView):

    serializer_class=UserCreationSerializer


class PostListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    def perform_create(self, serializer):

        return serializer.save(owner=self.request.user)
    
class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]



