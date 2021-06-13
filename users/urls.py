from django.urls import path
from users import views

urlpatterns = [

    path('register_user/', views.UserCreateView.as_view(), name='user-register'),
    path('read_users/', views.UserListView.as_view(), name='users-read'),
    path('user_profile/', views.user_profile, name='user-profile'),

]
