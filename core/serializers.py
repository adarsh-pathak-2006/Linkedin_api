from rest_framework.serializers import ModelSerializer
from .models import post, profile, comment

class homefeed_serializer(ModelSerializer):
    class Meta:
        model=post
        fields=['title', 'content', 'created_at', 'created_by']

class CreatePost_serializer(ModelSerializer):
    class Meta:
        model=post
        fields=['title', 'content', 'created_at']

class profile_serializer(ModelSerializer):
    class Meta:
        model=profile
        fields=['headline', 'bio', 'location']

class comment_view(ModelSerializer):
    class Meta:
        model=comment
        fields=['content','author', 'created_at']

class Comment_add(ModelSerializer):
    class Meta:
        model=comment
        fields=['content']
