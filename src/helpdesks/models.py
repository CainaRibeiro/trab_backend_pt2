from django.db import models

# Create your models here.

class Helpdesk(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    service_priority = models.IntegerField(null=False)