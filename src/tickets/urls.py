from django.urls import path
from .views import TicketDeleteView, TicketEditView, TicketListView, TicketView

urlpatterns = [
    path('create/', TicketView.as_view(), name='create_ticket'),
    path('list/', TicketListView.as_view(), name='list_tickets'),
    path('edit/<int:ticket_id>/', TicketEditView.as_view(), name='edit_ticket'),
    path('delete/<int:ticket_id>/', TicketDeleteView.as_view(), name='delete_ticket'),
]