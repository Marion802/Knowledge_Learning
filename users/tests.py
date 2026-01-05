from django.test import TestCase
from django.urls import reverse
from .models import User
from django.contrib.auth import authenticate


class UserRegistrationTest(TestCase):

    def test_user_registration_creates_inactive_user(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'testuser',
                'email': 'test@example.com',
                'password': 'password123'
            }
        )

        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username='testuser')
        self.assertFalse(user.is_active)


class UserLoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='activeuser',
            password='password123',
            is_active=True
        )

    def test_user_can_login(self):
        user = authenticate(
            username='activeuser',
            password='password123'
        )
        self.assertIsNotNone(user)

