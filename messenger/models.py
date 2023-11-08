from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE) 
    content = models.TextField(_("Content"))
    sended = models.DateTimeField(_("Sent"), auto_now=False, auto_now_add=True)
    
    class Meta:
        ordering = ("sended",)
    

class Thread(models.Model):
    users = models.ManyToManyField(User, verbose_name=_("Users"), related_name="threads")
    messages = models.ManyToManyField(Message, verbose_name=_("Messages"))