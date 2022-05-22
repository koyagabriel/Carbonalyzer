from django.urls import reverse
from rest_framework.test import APITestCase
from api.tests.factories import UserFactory
from api.models.user import User


class TestRegistration(APITestCase):

    def register(self, user_data):
        return self.client.post(reverse('registration'), user_data, format='json')

    def test_registration_of_new_user(self):
        user_data = UserFactory.get_raw_data()
        response = self.register(user_data)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(email=user_data["email"]).count())

    def test_registration_with_existing_email(self):
        user = UserFactory.create()
        user_count = User.objects.count()
        new_user_data = UserFactory.get_raw_data()
        new_user_data |= {'email': user.email}
        response = self.register(new_user_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['email'][0], 'user with this email already exists.')
        self.assertEqual(user_count, User.objects.count())

    def _run_test_for_missing_required_key(self, key, user_data, error_msg):
        response = self.register(user_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()[key][0], error_msg)

    def test_registration_with_missing_email_key(self):
        user_data = UserFactory.get_raw_data()
        del user_data['email']
        error_msg = 'This field is required.'

        self._run_test_for_missing_required_key('email', user_data, error_msg)

    def test_registration_with_missing_password_key(self):
        user_data = UserFactory.get_raw_data(set_password=False)
        error_msg = 'This field is required.'

        self._run_test_for_missing_required_key('password', user_data, error_msg)

    def test_password_is_hashed(self):
        user_data = UserFactory.get_raw_data()
        response = self.register(user_data)
        instance = User.objects.get(pk=response.json()['id'])

        self.assertNotEqual(user_data['password'], instance.password)

    def test_missing_username_value(self):
        """
        It should set the value of username to email if username is missing
        """
        user_data = UserFactory.get_raw_data()
        del user_data['username']
        response = self.register(user_data)

        self.assertEqual(response.json()['username'], user_data['email'])


class TestLogin(APITestCase):

    def test_login_with_right_credentials(self):
        user = UserFactory.build()
        user.set_password("password")
        user.save()

        login_data = {'email': user.email, 'password': 'password'}
        response = self.client.post(reverse('token'), login_data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.json())
        self.assertRegexpMatches(response.json()['access'], r"\w.\w.\w")

    def test_login_with_wrong_credentials(self):
        login_data = {'email': "wrong@email.com",  'password': 'wrong_password'}
        response = self.client.post(reverse('token'), login_data, format='json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['detail'], 'No active account found with the given credentials')

    def test_login_of_deactivated_account(self):
        user = UserFactory.build()
        user.set_password("password")
        user.is_active = False
        user.save()

        login_data = {'email': user.email, 'password': 'password'}
        response = self.client.post(reverse('token'), login_data, format='json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['detail'], 'No active account found with the given credentials')

    def test_login_of_active_deleted_account(self):
        user = UserFactory.build()
        user.set_password("password")
        user.deleted = True
        user.save()

        login_data = {'email': user.email, 'password': 'password'}
        response = self.client.post(reverse('token'), login_data, format='json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['detail'], 'No active account found with the given credentials')


