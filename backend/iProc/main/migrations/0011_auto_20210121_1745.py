# Generated by Django 3.1.4 on 2021-01-21 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210121_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='user',
            new_name='User',
        ),
    ]
