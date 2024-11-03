import json
from django.test import TestCase
from django.urls import reverse
from .models import Helpdesk

class HelpdeskTests(TestCase):
    def setUp(self):
        self.helpdesk = Helpdesk.objects.create(name="Support", email="support@example.com", service_priority=3)

    def test_helpdesk_creation(self):
        self.assertEqual(self.helpdesk.name, "Support")
        self.assertEqual(self.helpdesk.service_priority, 3)

    def test_get_helpdesk_by_priority_view(self):
        response = self.client.get(reverse('get_helpdesks'), { 'priority': 3 })
        response_data = json.loads(response.content.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["name"], "Support")
