# Generated by Django 3.0.3 on 2020-03-11 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0013_user_seed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_seed',
            old_name='username',
            new_name='user',
        ),
        migrations.AddField(
            model_name='user_seed',
            name='name',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
