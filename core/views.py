from django.shortcuts import render
from rest_framework.views import APIView
from .models import post, profile
from .serializers import homefeed_serializer, CreatePost_serializer, profile_serializer
from rest_framework.response import Response

class HomeFeed(APIView):
    def get(self, requeest):
        data=post.objects.all()
        serial=homefeed_serializer(data, many=True)
        return Response(serial.data)


class CreatePost(APIView):
    def get(self, request):
        data=post.objects.filter(created_by=request.user)
        serial=homefeed_serializer(data, many=True)
        return Response(serial.data)
    def post(self, request):
        serial=CreatePost_serializer(data=request.data)
        if serial.is_valid():
            serial.save(created_by=request.user)
            return Response(serial.data)


class Profile_view(APIView):
    def get(self, request):
        data=profile.objects.filter(user=request.user)
        serial=profile_serializer(data)
        return Response(serial.data)

    

        

