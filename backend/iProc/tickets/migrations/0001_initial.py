# Generated by Django 3.1.7 on 2021-04-01 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tickets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.CharField(max_length=255)),
                ('list_color', models.CharField(max_length=75)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rev_user_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_title', models.CharField(max_length=255)),
                ('ticket_content', models.TextField()),
                ('ticket_color', models.CharField(max_length=75)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=50)),
                ('ticket_types', models.CharField(choices=[('New_feature', 'New feature'), ('Data_Discrepancy', 'Data Discrepancy'), ('Software_bug', 'Software bug'), ('Custom_Analytics_request', 'Custom Analytics request'), ('Data_import_export_issue', 'Data import/export issue'), ('Other', 'Other')], default='Other', max_length=50)),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('resolved', 'resolved'), ('pending', 'pending'), ('in_progress', 'InProgress'), ('onhold', 'onHold')], default='pending', max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rev_user_ticket', to=settings.AUTH_USER_MODEL)),
                ('lst_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rev_list_tickets', to='tickets.list')),
                ('responsible_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rev_user_resperson', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_title', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('ticket_file', models.FileField(upload_to=tickets.models.UploadedTicketPath)),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rev_upload_ticket', to='tickets.ticket')),
                ('upload_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rev_user_upload', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IndexHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_index', models.CharField(max_length=255)),
                ('destination_index', models.CharField(max_length=255)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('lst_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rev_list_history', to='tickets.list')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_changed', models.CharField(blank=True, max_length=255, null=True)),
                ('change_type', models.CharField(default='modification', max_length=255)),
                ('pre_value', models.CharField(blank=True, max_length=255, null=True)),
                ('post_value', models.CharField(blank=True, max_length=255, null=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rev_ticket_history', to='tickets.ticket')),
            ],
        ),
    ]
