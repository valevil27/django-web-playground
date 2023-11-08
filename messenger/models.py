from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import m2m_changed


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    content = models.TextField(_("Content"))
    sended = models.DateTimeField(_("Sent"), auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ("sended",)


class Thread(models.Model):
    users = models.ManyToManyField(
        User, verbose_name=_("Users"), related_name="threads"
    )
    messages = models.ManyToManyField(Message, verbose_name=_("Messages"))


def messages_changed(sender, **kwargs):
    instance: Thread = kwargs.get("instance", "")
    action: str = kwargs.get("action", "")
    pk_set: set = kwargs.get("pk_set", set())
    unallowed_pk = set()
    if action == "pre_add":
        for pk in pk_set:
            message = Message.objects.get(pk=pk)
            if message.user not in instance.users.all():
                print(f"Ups, user {message.user} is not in the thread!")
                unallowed_pk.add(pk) #? We cant edit a set while iterating it
    pk_set.difference_update(unallowed_pk)


m2m_changed.connect(messages_changed, Thread.messages.through)
