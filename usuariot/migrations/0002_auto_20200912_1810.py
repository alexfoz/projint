# Generated by Django 3.1.1 on 2020-09-12 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_tickets_user'),
        ('usuariot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariot',
            name='ticketId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.tickets'),
        ),
    ]
