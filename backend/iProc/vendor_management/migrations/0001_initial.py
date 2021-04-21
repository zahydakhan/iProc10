# Generated by Django 3.1.7 on 2021-04-21 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_config', '0003_auto_20210421_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('last_modified_date', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendorcat_created_rev', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiversityClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('last_modified_date', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendordiversity_created_rev', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('last_modified_date', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendortrades_created_rev', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorBasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=255)),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=255)),
                ('contact_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('approval_status', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_cat_rev', to='vendor_management.categories')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendorbasic_created_rev', to=settings.AUTH_USER_MODEL)),
                ('diversity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendorbasic_diversity_rev', to='vendor_management.diversityclassification')),
                ('payment_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendorbasic_payterm_rev', to='basic_config.paymentterm')),
            ],
        ),
        migrations.CreateModel(
            name='VendorTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('last_modified_date', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendortag_created_rev', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_no', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('extra_comments', models.CharField(blank=True, max_length=255, null=True)),
                ('deadline', models.DateField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('request_status', models.CharField(blank=True, choices=[('Open', 'Open'), ('Expired', 'Expired'), ('Closed', 'Closed')], default='Open', max_length=50, null=True)),
                ('request_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_req_created', to=settings.AUTH_USER_MODEL)),
                ('requesting_site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_req_sites', to='basic_config.sites')),
            ],
        ),
        migrations.CreateModel(
            name='VendorFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('uploaded_at', models.DateField(default=django.utils.timezone.now)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_upload_user', to=settings.AUTH_USER_MODEL)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_fileupload', to='vendor_management.vendorbasicinfo')),
            ],
        ),
        migrations.AddField(
            model_name='vendorbasicinfo',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendorbasic_tag_rev', to='vendor_management.vendortags'),
        ),
        migrations.AddField(
            model_name='vendorbasicinfo',
            name='trades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendorbasic_trade', to='vendor_management.trades'),
        ),
        migrations.CreateModel(
            name='CertificatesAndLisences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=255)),
                ('registration_no', models.CharField(max_length=255)),
                ('aggregation_body', models.CharField(max_length=255)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('last_modified_date', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_cert_user', to=settings.AUTH_USER_MODEL)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_cert', to='vendor_management.vendorbasicinfo')),
            ],
        ),
    ]
