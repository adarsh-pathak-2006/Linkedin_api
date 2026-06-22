from django.db import models
from django.contrib.auth.models import User


class post(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(post, on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post
    
class skills(models.Model):
    name=models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name
    

class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    headline=models.CharField(max_length=300)
    bio=models.TextField()
    location=models.CharField(max_length=100)
    skill=models.ManyToManyField(skills, null=True)
    

    def __str__(self):
        return self.user.username


