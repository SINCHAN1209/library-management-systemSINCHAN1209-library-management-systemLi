# Generated by Django 5.1.1 on 2024-09-12 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reader',
            old_name='reference_address',
            new_name='reader_address',
        ),
        migrations.RenameField(
            model_name='reader',
            old_name='reference_contsct',
            new_name='reader_contsct',
        ),
        migrations.RenameField(
            model_name='reader',
            old_name='reference_name',
            new_name='reader_name',
        ),
    ]
