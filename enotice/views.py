from django.shortcuts import render
from django.http import HttpResponse
from enotice.models import Post
from advertisment.models import Adv
from django.utils import timezone

#rest_framework
from rest_framework.views import APIView
from enotice.serializers import PostSerializer, AdvSerializer
from rest_framework.response import Response

# Create your views here.

class PostList(APIView):
    def get(self,request):
        postlist = Post.objects.all()
        serializer = PostSerializer(postlist, many=True)
        return Response(serializer.data)

class AdvList(APIView):
    def get(self,request):
        advlist = Adv.objects.all()
        serializer = AdvSerializer(advlist, many=True)
        return Response(serializer.data)
