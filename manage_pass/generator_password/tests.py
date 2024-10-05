from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from generator_password.models import Password


class PasswordViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.password_entry = Password.objects.create(
            service_name="test_service",
            encrypted_password="encrypted_test_password"
        )

    def test_get_password_success(self):
        response = self.client.get(f'/password/{self.password_entry.service_name}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['service_name'], self.password_entry.service_name)
        self.assertEqual(response.data['password'], self.password_entry.encrypted_password)

    def test_get_password_not_found(self):
        response = self.client.get('/password/unknown_service/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Service not found')

    def test_post_password_create(self):
        new_service_name = "new_test_service"
        response = self.client.post(f'/password/{new_service_name}/')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('password', response.data)

        new_password_entry = Password.objects.get(service_name=new_service_name)
        self.assertEqual(new_password_entry.service_name, new_service_name)

    def test_post_password_update(self):
        response = self.client.post(f'/password/{self.password_entry.service_name}/')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('password', response.data)

        updated_password_entry = Password.objects.get(service_name=self.password_entry.service_name)
        self.assertEqual(updated_password_entry.service_name, self.password_entry.service_name)
        self.assertNotEqual(updated_password_entry.encrypted_password, 'encrypted_test_password')


class PasswordSearchViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        Password.objects.create(service_name="service_one", encrypted_password="password1")
        Password.objects.create(service_name="service_two", encrypted_password="password2")
        Password.objects.create(service_name="another_service", encrypted_password="password3")

    def test_search_passwords_success(self):
        response = self.client.get('/password/?service_name=service')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_search_passwords_no_match(self):
        response = self.client.get('/password/?service_name=nonexistent')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_search_without_param(self):
        response = self.client.get('password/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
