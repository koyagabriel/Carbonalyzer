from django.urls import reverse
from rest_framework.test import APITestCase
from api.tests.factories.user import UserFactory


class TestProfile(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = UserFactory.build()
        cls.user.set_password('password')
        cls.user.save()

        login_data = {'email': cls.user.email, 'password': 'password'}
        client = cls.client_class()
        response = client.post(reverse('token'), login_data, format='json')
        cls.access_token = response.json()['access']

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_get_user_profile(self):
        response = self.client.get(reverse('user_profile'), format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['email'], self.user.email)

    def test_user_profile_update(self):
        update_params = {'first_name': 'New firstname', 'last_name': 'New lastname'}
        response = self.client.patch(reverse('user_profile_update'), update_params, format='json')
        new_first_name = response.json()['first_name']
        new_last_name = response.json()['last_name']

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(self.user.first_name, new_first_name)
        self.assertNotEqual(self.user.last_name, new_last_name)