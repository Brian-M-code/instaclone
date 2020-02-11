from django.db import models
from django.contrib.auth.models import User
from vote.models import VoteModel


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    avatar = models.ImageField(blank=True,upload_to='prof_pics',default='default.png')
    bio = models.CharField(max_length=200)
    followers= models.ManyToManyField(User,related_name='followers', blank=True)
    following= models.ManyToManyField(User,related_name='following', blank=True)
    objects = models.Manager()

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
        
    def delete_image(self):
        self.delete()
        
    @classmethod    
    def update_caption(cls,id,new_caption):
        cls.objects.filter(pk = id ).update(image_caption = new_caption)
        new_caption_object = cls.objects.get(image_caption=new_caption)
        new_caption = new_caption_object.image_caption
        return new_caption
    

    @classmethod
    def get_all_images(cls):
        all_images=cls.objects.all()
        return all_images

    @classmethod
    def get_single_img(cls, id):
        one_img=cls.objects.filter(id=id)
        
class Comments(models.Model):
    comment = models.TextField(blank=True)
    image = models.ForeignKey(Image)
    user = models.ForeignKey(User)
    
    @classmethod
    def get_comments(cls,id):
        comment = cls.objects.filter(image__id=id)
        return comment
    
    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment

