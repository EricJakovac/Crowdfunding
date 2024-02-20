from django.test import TestCase
from main.models import User


class Testmodels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name = "first-name",
            last_name = "last-name",
            email = "e@mail.com",
    )

    def test_author(self):
        self.assertEquals(self.user.first_name, "first-name")