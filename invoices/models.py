from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Invoices(models.Model):
    number = models.CharField(max_length=25, blank=True)
    client = models.CharField("client", max_length=64, blank=True)
    path = models.CharField("path", max_length=64, blank=True)
    isDownload = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number
