# Generated by Django 3.1.1 on 2020-09-30 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0011_auto_20200924_0640'),
        ('feedBack', '0007_feedback_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
        ),
    ]
