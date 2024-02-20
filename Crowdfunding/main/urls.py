from django.urls import path
from . import views
from main.views import *

app_name = 'main' 

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('user/', UserList.as_view(), name='user_list'), 
    path('userprofile/', UserProfileList.as_view(), name='user_profile_list'),
    path('project/', ProjectList.as_view(), name='project_list'),
    path('donation/', DonationList.as_view(), name='donation_list'),
    path('support/', SupportList.as_view(), name='support_list'),
    path('register/', views.register, name='register'),
    path('add/', views.ProjectCreateView.as_view(), name='add'),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProjectDeleteView.as_view(), name='delete'),
    path('adduser/', views.UserCreateView.as_view(), name='adduser'),
]