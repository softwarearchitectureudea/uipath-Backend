from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Invoices
from .serializers import InvoicesSerializer


class InvoicesAPIView(generics.ListCreateAPIView):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer

