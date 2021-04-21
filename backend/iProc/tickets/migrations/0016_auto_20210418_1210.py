# Generated by Django 3.1.7 on 2021-04-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0015_auto_20210418_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('resolved', 'resolved'), ('pending', 'pending'), ('in_progress', 'InProgress')], default='pending', max_length=20),
        ),
    ]
