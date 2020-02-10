from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    avatar = ImageField(manual_crop='', null=True)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profile=cls.objects.all()

    @classmethod
    def single_profile(cls, id):
        single_profile = cls.objects.filter(id=id)
        return single_profile
    
class Image(models.Model):
    image = models.ImageField(null=True)
    name = models.CharField(max_length=30)
    caption = models.TextField(blank=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile, null=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def get_all_images(cls):
        all_images=cls.objects.all()
        return all_images

    @classmethod
    def get_single_img(cls, id):
        one_img=cls.objects.filter(id=id)

