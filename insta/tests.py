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
        
    def test_save_profile(self):
        self.testuseth=User(username='21xsavage')
        testprof=Profile(user=self.testuseth, avatar='', bio='WWWiii')
        testprof.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(Profile)>0)

    def test_single_profile(self, id):
        i_profile = Profile.single_profile(id=id)
        self.assertTrue(i_profile is not None)
