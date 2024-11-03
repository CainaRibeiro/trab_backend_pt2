from django.test import TestCase
from django.urls import reverse
from .models import Ticket, Helpdesk, User
from .forms import TicketForm, TicketEditForm

class TicketViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='testuser', email='email@teste.com')
        self.helpdesk = Helpdesk.objects.create(name="Support", email="support@example.com", service_priority=3)

    def test_create_ticket_view_get(self):
        response = self.client.get(reverse('create_ticket'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')
        self.assertIsInstance(response.context['form'], TicketForm)

    def test_create_ticket_view_post_valid(self):
        self.client.post(reverse('create_ticket'), {
            'ticket': 'Test Ticket',
            'description': 'Description of the ticket',
            'priority': 3,
            'helpdesk_id': self.helpdesk.id,
            'user_id': self.user.id,
        })
        
        self.assertEqual(Ticket.objects.count(), 1)

    def test_create_ticket_view_post_invalid(self):
        response = self.client.post(reverse('create_ticket'), {
            'ticket': '',
            'description': 'Description of the ticket',
            'priority': 3,
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')

class TicketListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='testuser', email='email@teste.com')
        self.helpdesk = Helpdesk.objects.create(name="Support", email="support@example.com", service_priority=3)
        Ticket.objects.create(ticket="Test Ticket", description="Description", priority=3, user_id=self.user, helpdesk_id=self.helpdesk)

    def test_ticket_list_view(self):
        response = self.client.get(reverse('list_tickets'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        self.assertEqual(len(response.context['tickets']), 1)

class TicketEditViewTests(TestCase):
    def setUp(self):
        self.helpdesk = Helpdesk.objects.create(name="Support", email="support@example.com", service_priority=3)
        self.ticket = Ticket.objects.create(ticket="Test Ticket", description="Description", priority=3, user_id=self.user, helpdesk_id=self.helpdesk)

    def test_edit_ticket_view_get(self):
        response = self.client.get(reverse('edit_ticket', args=[self.ticket.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_ticket.html')
        self.assertIsInstance(response.context['form'], TicketEditForm)

    def test_edit_ticket_view_post_valid(self):
        response = self.client.post(reverse('edit_ticket', args=[self.ticket.id]), {
            'ticket': 'Updated Ticket',
            'description': 'Updated Description',
            'priority': 'Medium',
            'helpdesk_id': self.helpdesk.id,
            'user_id': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.ticket.refresh_from_db()
        self.assertEqual(self.ticket.ticket, 'Updated Ticket')

    def test_edit_ticket_view_post_invalid(self):
        response = self.client.post(reverse('edit_ticket', args=[self.ticket.id]), {
            'ticket': '',
            'description': 'Updated Description',
            'priority': 'Medium',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_ticket.html')
        self.assertFormError(response, 'form', 'ticket', 'This field is required.')

class TicketDeleteViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='testuser', password='12345')
        self.helpdesk = Helpdesk.objects.create(name="Support", email="support@example.com", service_priority=3)
        self.ticket = Ticket.objects.create(ticket="Test Ticket", description="Description", priority=3, user_id=self.user, helpdesk_id=self.helpdesk)

    def test_delete_ticket_view(self):
        response = self.client.post(reverse('delete_ticket', args=[self.ticket.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('list_tickets'))
        self.assertEqual(Ticket.objects.count(), 0)
