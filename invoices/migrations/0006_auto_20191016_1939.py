# Generated by Django 2.2.6 on 2019-10-17 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0005_auto_20191016_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoices',
            old_name='path',
            new_name='file',
        ),
    ]
