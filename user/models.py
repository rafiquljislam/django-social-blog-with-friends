from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100,blank=True, null=True)
    image = models.ImageField(default='image/profile.png', upload_to='image/')
    friend = models.ManyToManyField('Profile', blank=True)
    slug = AutoSlugField(populate_from='user',blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

    
class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    timesend = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Form-{ self.from_user }-to-{self.to_user}"
    

