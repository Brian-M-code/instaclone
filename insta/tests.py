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
        
class UserTestClass(TestCase):
    def setUp(self):
        self.user = User(first_name="Brian", last_name="Mutuma",
                         username="brianmutuma", email="mutuma@gmail.com",)

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User(first_name="Brian", last_name="Mutuma",
                         username="brianmutuma", email="mutuma@gmail.com",)
        
        self.new_image = Image(id ='', name = 'art', caption = 'nairobi' user = self.brian)
        self.new_image.save()
    
    def test_save_method(self):
        self.new_image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(images) > 0)
        
    def test_delete_method(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(images) == 0)
        
    def test_update_method(self):
        self.new_image.save_image()
        self.new_image.update_caption()
        image = Image.objects.all()
        self.assertTrue(len(images) == 0)