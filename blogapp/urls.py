from django.urls import path
from blogapp import views


urlpatterns = [
    path('index/', views.IndexPageView.as_view()),
    path('', views.PostListView.as_view(), name='blog-post'),
    path('user_post/<username>/', views.UserPostListView.as_view(), name='user-post'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post_create/', views.PostCreateView.as_view(), name='post-create'),
    path('post_update/<int:pk>', views.PostUpdateView.as_view(), name='post-update'),
    path('post_delete/<int:pk>', views.PostDeleteView.as_view(), name='post-delete'),
    
    


]
