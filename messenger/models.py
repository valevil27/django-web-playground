from __future__ import annotations
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


class ThreadManager(models.Manager):
    # Inside the class, self = Thread.objects
    def find_by_users(self, *users: User) -> (Thread | None): 
        query = self.all()
        for user in users:
            query = query.filter(users=user)
            if len(query) == 0:
                return None
        return query.first()

    def find_or_create_by_users(self, *users: User):
        thread = self.find_by_users(*users)
        if thread: return thread
        new_thread: Thread = self.create()
        new_thread.users.add(*users)
        return new_thread
            

class Thread(models.Model):
    users = models.ManyToManyField(
        User, verbose_name=_("Users"), related_name="threads"
    )
    messages = models.ManyToManyField(Message, verbose_name=_("Messages"))
    objects = ThreadManager()


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
                unallowed_pk.add(pk)  # ? We cant edit a set while iterating it
    pk_set.difference_update(unallowed_pk)


m2m_changed.connect(messages_changed, Thread.messages.through)
