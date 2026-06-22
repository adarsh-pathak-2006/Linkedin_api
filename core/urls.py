from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', HomeFeed.as_view(), name='home'),
    path("home/<int:pk>/", individualpost.as_view(), name="individual"),
    path('home/<int:pk>/comment/', CommentView.as_view(), name='comment'),
    path('profile/', Profile_view.as_view(), name='profile'),
    path('create/', CreatePost.as_view(), name='create'),
]
