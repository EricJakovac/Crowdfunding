from django.shortcuts import render
from main.models import *
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

class UserList(ListView):
    model = User
    template_name = 'main/users_list.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.filter(is_staff=False)
    
class UserProfileList(ListView):
    model = UserProfile

class DonationList(ListView):
    model = Donation

class ProjectList(ListView):
    mdoel = Project

class SupportList(ListView):
    model = Support

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