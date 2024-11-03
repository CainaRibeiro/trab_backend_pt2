import json
from django.test import TestCase
from django.urls import reverse
from .models import User

class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="user", email="user@example.com")


    def test_get_users(self):
        response = self.client.get(reverse('get-users'))
        response_data = json.loads(response.content.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["name"], "user")
