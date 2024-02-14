import factory
from factory.django import DjangoModelFactory, ImageField
from django.contrib.auth.models import User
from django.utils import timezone
from main.models import *
from faker import Faker

fake = Faker()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: f'unique_username_{fake.uuid4()}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@example.com')
    first_name = factory.LazyAttribute(lambda _: fake.first_name())
    last_name = factory.LazyAttribute(lambda _: fake.last_name())
    password = factory.PostGenerationMethodCall('set_password', 'password123')

class UserProfileFactory(DjangoModelFactory):
    class Meta:
        model = UserProfile

    korisnik = factory.SubFactory(UserFactory)
    opis = factory.Faker('text')
    slika_profila = ImageField()

class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    naziv = factory.Faker('sentence')
    opis = factory.Faker('text')
    pocetak_kampanje = factory.Faker('date_time_this_year', tzinfo=timezone.get_current_timezone())
    zavrsetak_kampanje = factory.Faker('date_time_this_year', tzinfo=timezone.get_current_timezone())
    ciljani_iznos = factory.Faker('pydecimal', left_digits=5, right_digits=2)
    autor = factory.SubFactory(UserFactory)

class DonationFactory(DjangoModelFactory):
    class Meta:
        model = Donation

    iznos = factory.Faker('pydecimal', left_digits=5, right_digits=2)
    datum_donacije = factory.Faker('date_time_this_year', tzinfo=timezone.get_current_timezone())
    donator = factory.SubFactory(UserFactory)
    projekt = factory.SubFactory(ProjectFactory)

class SupportFactory(DjangoModelFactory):
    class Meta:
        model = Support

    korisnik = factory.SubFactory(UserFactory)
    projekt = factory.SubFactory(ProjectFactory)
    datum_podrske = factory.Faker('date_time_this_year', tzinfo=timezone.get_current_timezone())