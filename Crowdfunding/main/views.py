from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from main.models import *
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class UserList(ListView):
    model = User
    template_name = 'main/users_list.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.filter(is_staff=False)
    
class UserProfileList(ListView):
    model = UserProfile
    template_name = 'main/user_profile_list.html'
    context_object_name = 'user_profile_list'

    def get_queryset(self):
        return UserProfile.objects.all()
    
class ProjectList(ListView):
    model = Project
    template_name = 'main/project_list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.all()  

class DonationList(ListView):
    model = Donation
    template_name = 'main/donation_list.html'
    context_object_name = 'donation_list'

    def get_queryset(self):
        return Donation.objects.all()

class SupportList(ListView):
    model = Support
    template_name = 'main/support_list.html'
    context_object_name = 'support_list'

    def get_queryset(self):
        return Support.objects.all()
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:homepage')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)


def homepage(request):
    num_users = User.objects.exclude(is_staff=True).count()
    num_projects = Project.objects.all().count()
    num_donations = Donation.objects.all().count()

    context = {
        'num_users' : num_users,
        'num_projects' : num_projects,
        'num_donations' : num_donations,
    }

    return render(request, 'main/index.html', context=context)