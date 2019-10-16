from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'v1/invoices', views.InvoicesAPIView.as_view(), name='invoices-list'),
    path(r'v1/invoices/download', views.download_file, name='download'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
