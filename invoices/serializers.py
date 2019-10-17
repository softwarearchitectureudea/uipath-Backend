from rest_framework import serializers

from .models import Invoices, Payment


class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Payment
        fields = (
            'id', 'code', 'nit', 'amount'
        )

class RegisterPaymentsSerializer(serializers.Serializer):
    invoiceId = serializers.IntegerField()
    payments = PaymentSerializer(many=True)

    def validate(self, data):
        return data

    def create(self, validated_data):
        invoiceId = validated_data.pop('invoiceId')
        payments = validated_data.pop('payments')
        for payment in payments:
            Payment.objects.create(**payment,invoice_id=invoiceId)
        invoice=Invoices.objects.get(id=invoiceId)
        invoice.paid=True
        invoice.save()
        return invoice
