# Generated by Django 3.1.1 on 2020-09-17 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketstatus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketstatus',
            old_name='estatus',
            new_name='status',
        ),
    ]
