from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTeste(APITestCase):
    def test_register_accounts(self):
        url = reverse("registration")
        data = {
            "email": "teste@example.com",
            "name": "teste",
            "surname": "Teste",
            "password": "Teste@24",
            "password2": "Teste@24",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def test_register_accounts_doubled_erro(self):
            url = reverse("registration")
            data = {
                "email": "teste@example.com",
                "name": "teste",
                "surname": "Teste",
                "password": "Teste@24",
                "password2": "Teste@24",
            }
            response = self.client.post(url, data, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

            def test_register_accounts_hull_email_erro(self):
                url = reverse("registration")
                data = {
                    "email": " ",
                    "name": "teste",
                    "surname": "Teste",
                    "password": "Teste@24",
                    "password2": "Teste@24",
                }
                response = self.client.post(url, data, format="json")
                self.assertEqual(
                    response.status_code, status.HTTP_400_BAD_REQUEST
                )  # noaq: E%01

            def test_login(self):
                url = reverse("token_obtain_pair")
                data = {
                    "email": "teste@example.com",
                    "password": "Teste@24",
                }
                response = self.client.post(url, data, format="json")
                self.assertEqual(response.status_code, status.HTTP_200_OK)

            def test_login_password_wrong(self):
                url = reverse("token_obtain_pair")
                data = {
                    "email": "teste@example.com",
                    "password": "jjsajwnjeqm",
                }
                response = self.client.post(url, data, format="json")
                self.assertEqual(
                    response.status_code, status.HTTP_400_BAD_REQUEST
                )  # noaq: E%01

            def test_login_null_email(self):
                url = reverse("token_obtain_pair")
                data = {
                    "email": "teste@example.com",
                    "password": "Teste@24",
                }
                response = self.client.post(url, data, format="json")
                self.assertEqual(
                    response.status_code, status.HTTP_400_BAD_REQUEST
                )  # noaq: E%01
