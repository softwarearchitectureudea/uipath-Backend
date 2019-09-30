from django.urls import path

from . import views

urlpatterns = [
    path(r'v1/invoices', views.InvoicesAPIView.as_view(), name='invoices-list'),
    path(r'v1/invoices/download', views.download_file, name='download'),
]
