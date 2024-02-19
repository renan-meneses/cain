from django import reverse
from rest_framework import status
from rest_framework.test import APIClient


class EnterprisesTeste(APIClient):
    def test_create_enterprise(self):
        url = reverse("enterprise")
        data = {
            "cnpj": "00416968000101",
            "corporate": "BANCO INTER S.A",
            "fantasy": "BANCO INTER S.A",
            "associates": ["1"],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_erro_enterprise(self):
        url = reverse("enterprise")
        data = {
            "cnpj": "00416968000101",
            "corporate": "BANCO INTER S.A",
            "fantasy": "BANCO INTER S.A",
            "associates": ["1"],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_erro_enterprise_null_cnpj(self):
        url = reverse("enterprise")
        data = {
            "cnpj": "",
            "corporate": "BANCO INTER S.A",
            "fantasy": "BANCO INTER S.A",
            "associates": ["1"],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_enterprise(self):
        url = reverse("enterprise")
        data = {
            "cnpj": "",
            "corporate": "BANCO INTER S.A",
            "fantasy": "BANCO INTER S.A",
            "associates": ["1"],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
