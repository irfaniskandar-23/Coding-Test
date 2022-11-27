from django.test import TestCase
from django.urls import reverse
from django.urls import resolve


# Create your tests here.


class InventoryTest(TestCase):
    def test_url_view(self):
        response = self.client.get("/inventory/")
        self.assertEqual(response.status_code, 200)

    def test_url_api(self):
        response = self.client.get("/api/inventory/")
        self.assertEqual(response.status_code, 200)
