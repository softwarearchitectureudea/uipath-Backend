import csv
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Invoices
from .serializers import InvoicesSerializer


class InvoicesAPIView(generics.ListCreateAPIView):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer


def download_file(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="invoices-ID.csv"'

    writer = csv.writer(response)
    writer.writerow(['nit', 'valor', 'fecha',])

    return response
