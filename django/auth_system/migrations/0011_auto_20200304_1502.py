# Generated by Django 3.0.3 on 2020-03-04 07:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0010_auto_20200304_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 4, 7, 2, 9, 787415, tzinfo=utc)),
        ),
    ]
