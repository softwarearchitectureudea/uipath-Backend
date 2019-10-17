from django.contrib import admin
from invoices.models import Invoices
# Register your models here.

@admin.register(Invoices)
class HeroAdmin(admin.ModelAdmin):
    readonly_fields = ["paid"]

