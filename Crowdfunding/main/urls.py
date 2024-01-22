from django.urls import path
from . import views
from main.views import *

app_name = 'main' 

urlpatterns = [
    path('', views.homepage, name='homepage'),

]