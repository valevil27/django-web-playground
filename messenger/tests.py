from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message


# Create your tests here.
class ThreadTest(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create_user("one", None, "test1234")
        self.user2 = User.objects.create_user("two", None, "test1234")
        self.user3 = User.objects.create_user("three", None, "test1234")

        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()), 2, "Users not added to thread")

    def test_filter_thread_by_users(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread, threads.first(), "Can't filter thread by users")

    def test_add_msg_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Hello there")
        message2 = Message.objects.create(user=self.user2, content="General Kenobi")

        self.thread.messages.add(message1, message2)
        self.assertEqual(
            len(self.thread.messages.all()), 2, "Messages not added to the Thread"
        )

    def test_user_outsider_put_message_in_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Hello there")
        message2 = Message.objects.create(user=self.user2, content="General Kenobi")
        message3 = Message.objects.create(
            user=self.user3, content="Pikachu I choose you!"
        )
        self.thread.messages.add(message1, message2, message3)
        self.assertEqual(
            len(self.thread.messages.all()), 2, "Outsider users can post in thread"
        )

    def test_find_thread_by_user_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find_by_users(self.user1, self.user2) # type: ignore
        self.assertEqual(
            self.thread, thread, "Can't filter thread by users using custom manager"
        )

    def test_find_or_create_thread_by_user_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find_or_create_by_users(self.user1, self.user2) # type: ignore
        self.assertEqual(
            self.thread, thread, "Can't find thread by users using custom find_or_create"
        )
        thread = Thread.objects.find_or_create_by_users(self.user1, self.user2, self.user3) # type: ignore
        self.assertIsNotNone(thread, "Can't create the thread using find_or_create")