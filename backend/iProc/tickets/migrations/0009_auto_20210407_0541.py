# Generated by Django 3.1.7 on 2021-04-07 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20210406_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='lst_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='revlisttickets', to='tickets.list'),
        ),
    ]
