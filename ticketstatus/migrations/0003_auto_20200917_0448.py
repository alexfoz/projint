# Generated by Django 3.1.1 on 2020-09-17 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketstatus', '0002_auto_20200917_0441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketstatus',
            name='status',
        ),
        migrations.AddField(
            model_name='ticketstatus',
            name='estatus',
            field=models.TextField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
