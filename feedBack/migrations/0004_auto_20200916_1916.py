# Generated by Django 3.1.1 on 2020-09-16 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedBack', '0003_auto_20200916_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='responsavelbas',
            new_name='responsavel',
        ),
    ]
