from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.testuser=User(username='Cole')

        self.testProfile=Profile(user=self.testuser, avatar='', bio='WWWiii')
        self.testProfile.save_profile()

    def test_instance_profile(self):
        self.assertTrue(isinstance(self.testProfile, Profile))
