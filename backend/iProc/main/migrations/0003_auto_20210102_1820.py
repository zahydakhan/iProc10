# Generated by Django 3.1.4 on 2021-01-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210102_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedata',
            name='DATE_ENTERED',
            field=models.DateField(auto_now_add=True),
        ),
    ]