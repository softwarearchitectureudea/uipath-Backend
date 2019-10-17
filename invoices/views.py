from django.http import HttpResponse, Http404
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Invoices
from .serializers import InvoicesSerializer, RegisterPaymentsSerializer


class InvoicesAPIView(generics.ListCreateAPIView):
    queryset = Invoices.objects.all().order_by('paid')
    serializer_class = InvoicesSerializer


def download_file(request):
    obj_id=request.GET['id']
    try:
        obj=Invoices.objects.get(id=obj_id)
        response = HttpResponse(obj.file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=factura.csv'
        return response
    except:
        raise Http404("Invoice does not exist")

class PaymentsAPIView(GenericAPIView):
    serializer_class = RegisterPaymentsSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterPaymentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'saved': True
        }

        return Response(data=data, status=status.HTTP_201_CREATED)

