from django.db import models
from helpdesks.models import Helpdesk
from users.models import User

# Create your models here.

class Ticket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    helpdesk_id = models.ForeignKey(Helpdesk, on_delete=models.CASCADE, related_name='tickets')
    ticket = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=400, null=False)
    priority = models.IntegerField(null=False)
    resolution = models.CharField(max_length=300, null=True)