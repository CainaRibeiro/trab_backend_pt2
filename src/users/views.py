from django.http import JsonResponse
from django.views.generic import View

from users.models import User

# Create your views here.

class UserView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all().values("id", "name")
        return JsonResponse(list(users), safe=False)