from django.urls import path
from .views import TicketView

urlpatterns = [
    path('create/', TicketView.as_view(), name='create_ticket'),
]