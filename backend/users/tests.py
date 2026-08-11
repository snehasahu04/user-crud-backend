from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import UserProfile


class JWTAuthTests(APITestCase):
    def test_register_creates_user_without_tokens(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'StrongPass123',
            'first_name': 'Test',
            'last_name': 'User',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'User registered successfully')
        self.assertEqual(response.data['user']['email'], 'test@example.com')

    def test_login_returns_tokens_for_existing_user(self):
        user_model = get_user_model()
        user_model.objects.create_user(
            username='loginuser',
            email='login@example.com',
            password='StrongPass123',
        )

        url = reverse('token_obtain_pair')
        response = self.client.post(
            url,
            {'email': 'login@example.com', 'password': 'StrongPass123'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_list_returns_only_authenticated_user_profile(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username='owner',
            email='owner@example.com',
            password='StrongPass123',
        )

        UserProfile.objects.create(
            first_name='Owner',
            last_name='User',
            email='owner@example.com',
        )
        UserProfile.objects.create(
            first_name='Other',
            last_name='User',
            email='other@example.com',
        )

        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('user-list-create'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['email'], 'owner@example.com')
