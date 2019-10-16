import csv
import os

from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import generics
from .models import Invoices
from .serializers import InvoicesSerializer
from django.conf import settings
from django.http import FileResponse


class InvoicesAPIView(generics.ListCreateAPIView):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer


def download_file(request):
    obj_id=request.GET['id']
    try:
        obj=Invoices.objects.get(id=obj_id)
        response = HttpResponse(obj.path, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=factura.csv'
        return response
    except:
        raise Http404("Invoice does not exist")

