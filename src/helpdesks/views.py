from django.http import JsonResponse
from django.views import View
from .models import Helpdesk

class HelpdeskByPriorityView(View):
    def get(self, request, *args, **kwargs):
        priority = request.GET.get("priority")
        helpdesks = Helpdesk.objects.filter(service_priority=priority).values("id", "name")
        return JsonResponse(list(helpdesks), safe=False)
