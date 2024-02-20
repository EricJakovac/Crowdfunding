from django.test import TestCase
from django.urls import reverse
from main.models import User, Project, Donation
from main.views import homepage
from datetime import datetime

class TestViews(TestCase):
    def setUp(self):
        # Set up test data
        self.user1 = User.objects.create(username='testuser1', email='test1@example.com')
        self.user2 = User.objects.create(username='testuser2', email='test2@example.com')
        self.project1 = Project.objects.create(
            naziv='Project 1', 
            opis='Description 1', 
            autor=self.user1, 
            pocetak_kampanje=datetime.now()  # Provide a valid value for pocetak_kampanje
        )
        self.project2 = Project.objects.create(
            naziv='Project 2', 
            opis='Description 2', 
            autor=self.user2, 
            pocetak_kampanje=datetime.now()  # Provide a valid value for pocetak_kampanje
        )
        self.donation1 = Donation.objects.create(iznos=100, donator=self.user1, projekt=self.project1)
        self.donation2 = Donation.objects.create(iznos=200, donator=self.user2, projekt=self.project2)
