# Generated by Django 3.1.1 on 2020-09-24 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_auto_20200924_0554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='isAtivo',
        ),
    ]
