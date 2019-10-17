from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Invoices(models.Model):
    number = models.CharField(max_length=25, blank=True)
    file = models.FileField(upload_to='files')
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number
