# Generated by Django 3.1.1 on 2020-09-30 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedBack', '0006_auto_20200924_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='nome',
            field=models.CharField(db_column=False, default='', max_length=120),
            preserve_default=False,
        ),
    ]
