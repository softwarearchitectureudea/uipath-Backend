# Generated by Django 2.2.6 on 2019-10-17 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_auto_20191015_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoices',
            old_name='createdAt',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='invoices',
            old_name='isDownload',
            new_name='paid',
        ),
        migrations.RenameField(
            model_name='invoices',
            old_name='updatedAt',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='client',
        ),
    ]
