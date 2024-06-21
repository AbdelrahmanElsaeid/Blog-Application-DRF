# tests.py
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile

class AuthTests(APITestCase):

    def setUp(self):
        self.signup_url = reverse('signup')
        self.login_url = reverse('rest_login')
        self.logout_url = reverse('rest_logout')
        self.profile_url = reverse('profile-detail')
        
        self.user_data = {
            'username': 'testuser',
            'password': 'Test12345',
            'email': 'testuser@example.com'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.profile = Profile.objects.get(user=self.user)

    def test_signup(self):
        data = {
            'username': 'newuser',
            'password': 'Test12345',
            'password2': 'Test12345',
            'email': 'newuser@example.com'
        }
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())

  
    def test_login(self):
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)
        access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)    

    def test_logout(self):
        self.test_login()
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_retrieve(self):
        self.test_login()
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], self.profile.bio)

    def test_profile_update(self):
        self.test_login()
        data = {'bio': 'Updated bio'}
        response = self.client.put(self.profile_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.bio, 'Updated bio')

    def test_profile_delete(self):
        self.test_login()
        response = self.client.delete(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Profile.objects.filter(user=self.user).exists())
        self.assertFalse(User.objects.filter(username='testuser').exists())
