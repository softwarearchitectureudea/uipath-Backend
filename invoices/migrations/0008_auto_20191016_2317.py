# Generated by Django 2.2.6 on 2019-10-17 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0007_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.Invoices'),
        ),
    ]
