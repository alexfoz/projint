# Generated by Django 3.1.1 on 2020-09-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_tickets_assunto'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='dataCriacao',
            field=models.DateField(max_length=10),
        ),
        migrations.AddField(
            model_name='tickets',
            name='dataFim',
            field=models.DateField(max_length=10),
        ),
    ]