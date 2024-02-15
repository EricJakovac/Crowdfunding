import random
from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import *
from main.factories import *

NUM_USERS = 40
NUM_USERS_PROFILES = 40
NUM_PROJECTS = 15
NUM_DONATIONS = 50
NUM_SUPPORTS = 30

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        
        self.stdout.write("Deleting old data...")
        
        models_to_delete = [UserProfile, Project, Donation, Support]
        users_to_delete = User.objects.exclude(is_superuser=True).all()

        for user in users_to_delete:
            self.stdout.write(f"Deleting user: {user.first_name} {user.last_name}")
            user.delete()

        for model in models_to_delete:
            model.objects.all().delete()

        self.stdout.write("Creating new data...")

        users = []
        for _ in range(NUM_USERS):
            user = UserFactory()
            users.append(user)

        for user in users:
            user_profile = UserProfileFactory(korisnik=user)

        for _ in range(NUM_PROJECTS):
            project = ProjectFactory(autor=random.choice(users))

        for _ in range(NUM_DONATIONS):
            donation = DonationFactory(donator=random.choice(users), projekt=random.choice(Project.objects.all()))

        for _ in range(NUM_SUPPORTS):
            support = SupportFactory(korisnik=random.choice(users), projekt=random.choice(Project.objects.all()))

        self.stdout.write(self.style.SUCCESS("Test data generated successfully."))
