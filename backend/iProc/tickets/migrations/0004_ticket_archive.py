# Generated by Django 3.1.7 on 2021-04-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20210402_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='archive',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Archive', 'Archive')], default='Active', max_length=50, null=True),
        ),
    ]
