# Generated by Django 3.0.3 on 2020-03-04 06:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0005_auto_20200304_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 4, 6, 3, 26, 24328, tzinfo=utc)),
        ),
    ]