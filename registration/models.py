from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) # type: ignore
    avatar = models.ImageField("Avatar", upload_to="profile_images", null=True, blank=True)
    bio = models.TextField("Biografía", null=True,blank=True)
    link = models.URLField("Portfolio", max_length=254, null=True, blank=True)