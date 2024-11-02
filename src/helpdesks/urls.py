from django.urls import path

from helpdesks.views import HelpdeskByPriorityView

urlpatterns = [
    path('get-by-priority/', HelpdeskByPriorityView.as_view(), name='get_helpdesks'),
]