from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) # type: ignore
    avatar = models.ImageField("Avatar", upload_to="profile_images", null=True, blank=True)
    bio = models.TextField("Biografía", null=True,blank=True)
    link = models.URLField("Portfolio", max_length=254, null=True, blank=True)
    
@receiver(post_save, sender=User)
def profile_on_user_creation(sender, instance, **kwargs):
    if kwargs.get("created", False):
        Profile.objects.get_or_create(user=instance)
        print("Se ha creado un usuario y un perfil enlazado.")
    