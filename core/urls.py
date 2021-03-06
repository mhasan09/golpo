"""Golpo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from core import views
from core import api
urlpatterns = [
    path('', views.feed, name="feed"),
    path('signin/', views.signin, name="signin"),
    path('api/add_post/', api.api_POST, name="api_add_post"),
    path('api/add_likes/', api.api_add_likes, name="api_add_likes"),
    path('profile/<str:username>', views.profile, name="profile"),
    path('profile/<str:username>/follow', views.follow_profile, name="follow_profile"),
    path('profile/<str:username>/unfollow', views.unfollow_profile, name="unfollow_profile"),
    path('followers/<str:username>', views.followers, name="followers"),
    path('follows/<str:username>', views.follows, name="follows"),
    path('edit/', views.edit_profile, name="edit_profile"),


]
