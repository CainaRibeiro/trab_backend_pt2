from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from tickets.forms import TicketEditForm, TicketForm
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
            else:
                return render(request, 'create.html', {'form': form})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
class TicketListView(View):
    def get(self, request, *args, **kwargs):
        tickets = Ticket.objects.select_related('user_id', 'helpdesk_id').all()
        
        return render(request, 'list.html', {'tickets': tickets})
    
class TicketEditView(View):
    def get(self, request, ticket_id, *args, **kwargs):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        form = TicketForm(instance=ticket)
        return render(request, 'edit_ticket.html', {'form': form, 'ticket': ticket})

    def post(self, request, ticket_id, *args, **kwargs):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        form = TicketEditForm(request.POST, instance=ticket)

        if form.is_valid():
            form.save()
            return redirect('list_tickets') 

        return render(request, 'edit_ticket.html', {'form': form, 'ticket': ticket})
    
class TicketDeleteView(View):
    def post(self, request, ticket_id, *args, **kwargs):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket.delete()
        return redirect('list_tickets')