from django import forms

from tickets.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket', 'description', 'priority', 'helpdesk_id', 'user_id']
        

class TicketEditForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['resolution'] 