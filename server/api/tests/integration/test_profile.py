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

    def get_profile(self):
        return self.client.get(reverse('user_profile'), format='json')

    def test_get_user_profile(self):
        response = self.get_profile()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['email'], self.user.email)

    def test_get_user_profile_for_deleted_account(self):
        self.user.deleted = True
        self.user.is_active = True
        self.user.save()
        response = self.get_profile()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['detail'], 'User not found')

    def test_get_user_profile_for_deactivated_account(self):
        self.user.is_active = False
        self.user.deleted = False
        self.user.save()
        response = self.get_profile()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['detail'], 'User is inactive')

    def test_user_profile_update(self):
        update_params = {'first_name': 'New firstname', 'last_name': 'New lastname'}
        response = self.client.patch(reverse('user_profile_update'), update_params, format='json')
        new_first_name = response.json()['first_name']
        new_last_name = response.json()['last_name']

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(self.user.first_name, new_first_name)
        self.assertNotEqual(self.user.last_name, new_last_name)