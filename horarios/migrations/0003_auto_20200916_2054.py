# Generated by Django 3.1.1 on 2020-09-16 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horarios', '0002_auto_20200916_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horarios',
            old_name='Horario',
            new_name='horario',
        ),
    ]
