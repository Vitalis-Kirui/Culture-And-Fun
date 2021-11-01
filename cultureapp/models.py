from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.IntegerField(default=0)
    profile_pic = CloudinaryField('profile')
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username