from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView,
    PostCreateAPIView)

urlpatterns = [

    path('', PostListAPIView.as_view(), name='api-list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>', PostDetailAPIView.as_view(), name='detail'),
    path('delete/<int:pk>', PostDeleteAPIView.as_view(), name='delete'),
    path('update/<int:pk>', PostUpdateAPIView.as_view(), name='update'),
    


]
