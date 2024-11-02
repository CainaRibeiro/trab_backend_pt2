from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from tickets.forms import TicketForm
from .models import Ticket

class TicketView(CreateView):
    model = Ticket
    template_name = 'create.html'
    success_url = reverse_lazy('dashboard')
    form_class = TicketForm
    
    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        try:
            form = TicketForm(request.POST)

            if form.is_valid():
                ticket = Ticket(
                    ticket=form.cleaned_data['ticket'],
                    description=form.cleaned_data['description'],
                    priority=form.cleaned_data['priority'],
                    helpdesk_id=form.cleaned_data.get('helpdesk_id'),
                    user_id=form.cleaned_data.get('user_id'),
                )

                ticket.save()
                return redirect('dashboard')

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)