from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import homepage, UserList, UserProfileList, ProjectList, DonationList, SupportList


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('main:homepage')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, homepage)

    def test_users_url_is_resolved(self):
        url = reverse('main:user_list')

        self.assertEquals(resolve(url).func.view_class, UserList)

    def test_userprofile_url_is_resolved(self):
        url = reverse('main:user_profile_list')

        self.assertEquals(resolve(url).func.view_class, UserProfileList)

    def test_projects_url_is_resolved(self):
        url = reverse('main:project_list')

        self.assertEquals(resolve(url).func.view_class, ProjectList)

    def test_donations_url_is_resolved(self):
        url = reverse('main:donation_list')

        self.assertEquals(resolve(url).func.view_class, DonationList)

    def test_Support_url_is_resolved(self):
        url = reverse('main:support_list')

        self.assertEquals(resolve(url).func.view_class, SupportList)