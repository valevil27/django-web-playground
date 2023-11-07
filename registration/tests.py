from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    #? Prepara las pruebas
    def setUp(self):
        User.objects.create_user("test","test@test.com","test1234")
    
    #? Realiza la prueba indicada
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists,True)
