from django.contrib import admin
from invoices.models import Invoices, Payment
# Register your models here.

@admin.register(Invoices)
class InvoicesAdmin(admin.ModelAdmin):
    readonly_fields = ["paid"]
    list_display = ("number","file","paid","created_at")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("code","nit","amount","invoice","created_at")

