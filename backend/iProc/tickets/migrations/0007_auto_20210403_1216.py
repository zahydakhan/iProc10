# Generated by Django 3.1.7 on 2021-04-03 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20210403_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='lst_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rev_list_tickets', to='tickets.list'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_types',
            field=models.CharField(choices=[('New_feature', 'New feature'), ('Data_Discrepancy', 'Data Discrepancy'), ('Software_bug', 'Software bug'), ('Custom_Analytics_request', 'Custom Analytics request'), ('Data_import_export_issue', 'Data import/export issue'), ('other', 'other')], default='Other', max_length=50),
        ),
    ]