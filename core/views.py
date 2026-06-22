from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from .models import post, profile, comment
from .serializers import homefeed_serializer, CreatePost_serializer, profile_serializer, comment_view, Comment_add
from rest_framework.response import Response
from django.views import View
from .forms import registerform
from django.contrib.auth.models import User



class RegisterView(View):
    def get(self, request):
        form=registerform
        return render(request, 'register.html', { 'form':form })

    def post(self, request):
        form_data=registerform(request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data['username']
            pass1=form_data.cleaned_data['password']
            pass2=form_data.cleaned_data['rep_password']

            if pass1==pass2:
                if User.objects.filter(username=name).exists():
                    return render(request, 'register.html', { 'user_err':'user already exist' })
                else:
                    User.objects.create_user(username=name, password=pass1)
                    return redirect('register')
            else:
                return render(request, 'register.html', { 'pass_err':'enter the same password in both the password fields' })
        else:
            return render(request, 'register.html', { 'invalid':'invalid input' })

class HomeFeed(APIView):
    def get(self, request):
        data=post.objects.all()
        serial=homefeed_serializer(data, many=True)
        return Response(serial.data)
    
class individualpost(APIView):
    def get(self, request, pk):
        data=get_object_or_404(post, id=pk)
        serial=homefeed_serializer(data)
        return Response(serial.data)
            

class CommentView(APIView):
    def get(self, request, pk):
        post_data=get_object_or_404(post,id=pk)
        data=comment.objects.filter(post=post_data)
        serial=comment_view(data, many=True)
        return Response(serial.data)

    def post(self, request, pk):
        post_data=get_object_or_404(post,id=pk)
        serial=Comment_add(data=request.data)
        if serial.is_valid():
            serial.save(author=request.user,
                        post=post_data)
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
        data=profile.objects.get(user=request.user)
        serial=profile_serializer(data)
        return Response(serial.data)
    


    

        

