"""Social_Media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views


app_name='S_M'
urlpatterns = [
    path('',views.ListPost.as_view(),name='dashboard' ),
    path('accounts/signup/',views.SignUpView.as_view(),name='signup'),
    path('profiles/',views.ListProfiles.as_view(),name='profiles'),
    path('user_profile/<int:pk>/',views.UserProfile.as_view(),name='user_profile'),
    path('follow/<int:id>',views.follow,name='follow'),
    path('un_follow/<int:id>',views.un_follow,name='un_follow'),
    path('create_post/',views.CreatePost.as_view(),name='create_post'),
    path('comment/<int:pk>',views.Comment.as_view(),name='comment'),

]
