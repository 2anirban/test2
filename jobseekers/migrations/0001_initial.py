# Generated by Django 3.1.3 on 2020-11-28 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='jobseekers',
            fields=[
                ('jseekers_id', models.AutoField(primary_key=True, serialize=False)),
                ('jseekers_firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('jseekers_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('jseekers_password', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_pic', models.ImageField(blank=True, null=True, upload_to='static/profilepics')),
                ('jseekers_headline', models.CharField(blank=True, max_length=4000, null=True)),
                ('jseekers_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('jseekers_gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('jseekers_location', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_otherinfo', models.CharField(blank=True, max_length=2000, null=True)),
                ('jseekers_industry', models.CharField(blank=True, choices=[('Select', 'Select'), ('Construction / Engineering / Cement / Metals', 'Construction / Engineering / Cement / Metals'), ('Consumer Durables', 'Consumer Durables'), ('FMCG/Food/Beverages', 'FMCG/Food/Beverages'), ('IT Software', 'IT Software'), ('IT Hardware', 'IT Hardware'), ('KPO/Research & Analytics', 'KPO/Research & Analytics'), ('Internet/Ecommerce', 'Internet/Ecommerce'), ('BPO', 'BPO'), ('Strategy /Management Consulting', 'Strategy /Management Consulting'), ('Textiles / Garments / Accessories', 'Textiles / Garments / Accessories'), ('Information Technology', 'Information Technology'), ('Software Application/Web Development', 'Software Application/Web Development'), ('Accounts', 'Accounts'), ('Medical& Healthcare', 'Medical& Healthcare')], max_length=200, null=True)),
                ('jseekers_functions', models.CharField(blank=True, choices=[('Select', 'Select'), ('Accounting / Tax / Company Secretary / Audit', 'Accounting / Tax / Company Secretary / Audit'), ('Analytics & Business Intelligence', 'Analytics & Business Intelligence'), ('Corporate Planning / Consulting / Strategy', 'Corporate Planning / Consulting / Strategy'), ('Entrepreneur / Businessman / Outside Management Consultant', 'Entrepreneur / Businessman / Outside Management Consultant'), ('HR / Admin / PM / IR / Training', 'HR / Admin / PM / IR / Training'), ('ITES / BPO / Operations', 'ITES / BPO / Operations'), ('Medical Professional / Healthcare Practitioner / Technician', 'Medical Professional / Healthcare Practitioner / Technician'), ('Mktg / Advtg  Media Planning / PR / Corp. Comm', 'Mktg / Advtg  Media Planning / PR / Corp. Comm'), ('R&D / Engineering Design', 'R&D / Engineering Design'), ('Sales / Business Development / Client Servicing', 'Sales / Business Development / Client Servicing'), ('Software Development - ALL', 'Software Development - ALL'), ('Software Development - Application Programming', 'Software Development - Application Programming'), ('Software Development - e-commerce / Internet Technologies', 'Software Development - e-commerce / Internet Technologies'), ('Software Development - Database Administration', 'Software Development - Database Administration'), ('Software Development - Embedded Technologies', 'Software Development - Embedded Technologies'), ('Software Development - ERP / CRM', 'Software Development - ERP / CRM'), ('Top Management', 'Top Management'), ('Others', 'Others'), ('Customer Relation Management', 'Customer Relation Management'), ('Finance & Accounting Operations', 'Finance & Accounting Operations')], max_length=200, null=True)),
                ('jseekers_workex', models.IntegerField(blank=True, null=True)),
                ('jseekers_currentorg', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_currentdesig', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_currentcv', models.FileField(blank=True, null=True, upload_to='media/cv')),
                ('jseekers_prev_industry', models.CharField(blank=True, choices=[('Select', 'Select'), ('Construction / Engineering / Cement / Metals', 'Construction / Engineering / Cement / Metals'), ('Consumer Durables', 'Consumer Durables'), ('FMCG/Food/Beverages', 'FMCG/Food/Beverages'), ('IT Software', 'IT Software'), ('IT Hardware', 'IT Hardware'), ('KPO/Research & Analytics', 'KPO/Research & Analytics'), ('Internet/Ecommerce', 'Internet/Ecommerce'), ('BPO', 'BPO'), ('Strategy /Management Consulting', 'Strategy /Management Consulting'), ('Textiles / Garments / Accessories', 'Textiles / Garments / Accessories'), ('Information Technology', 'Information Technology'), ('Software Application/Web Development', 'Software Application/Web Development'), ('Accounts', 'Accounts'), ('Medical& Healthcare', 'Medical& Healthcare')], max_length=200, null=True)),
                ('jseekers_prev_functions', models.CharField(blank=True, choices=[('Select', 'Select'), ('Accounting / Tax / Company Secretary / Audit', 'Accounting / Tax / Company Secretary / Audit'), ('Analytics & Business Intelligence', 'Analytics & Business Intelligence'), ('Corporate Planning / Consulting / Strategy', 'Corporate Planning / Consulting / Strategy'), ('Entrepreneur / Businessman / Outside Management Consultant', 'Entrepreneur / Businessman / Outside Management Consultant'), ('HR / Admin / PM / IR / Training', 'HR / Admin / PM / IR / Training'), ('ITES / BPO / Operations', 'ITES / BPO / Operations'), ('Medical Professional / Healthcare Practitioner / Technician', 'Medical Professional / Healthcare Practitioner / Technician'), ('Mktg / Advtg  Media Planning / PR / Corp. Comm', 'Mktg / Advtg  Media Planning / PR / Corp. Comm'), ('R&D / Engineering Design', 'R&D / Engineering Design'), ('Sales / Business Development / Client Servicing', 'Sales / Business Development / Client Servicing'), ('Software Development - ALL', 'Software Development - ALL'), ('Software Development - Application Programming', 'Software Development - Application Programming'), ('Software Development - e-commerce / Internet Technologies', 'Software Development - e-commerce / Internet Technologies'), ('Software Development - Database Administration', 'Software Development - Database Administration'), ('Software Development - Embedded Technologies', 'Software Development - Embedded Technologies'), ('Software Development - ERP / CRM', 'Software Development - ERP / CRM'), ('Top Management', 'Top Management'), ('Others', 'Others'), ('Customer Relation Management', 'Customer Relation Management'), ('Finance & Accounting Operations', 'Finance & Accounting Operations')], max_length=200, null=True)),
                ('jseekers_prev_org', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_prev_desig', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_prev_responsibilities', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_prev_joiningdate', models.DateField(blank=True, max_length=50, null=True)),
                ('jseekers_prev_relievingdate', models.DateField(blank=True, max_length=50, null=True)),
                ('jseekers_prev_summary', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_school', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_degree', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_datesattended', models.DateField(blank=True, max_length=200, null=True)),
                ('jseekers_field_study', models.CharField(blank=True, max_length=200, null=True)),
                ('jseekers_achievement', models.CharField(blank=True, max_length=2000, null=True)),
                ('jseekers_passion', models.CharField(blank=True, max_length=4000, null=True)),
                ('jseekers_timestamp', models.DateTimeField(auto_now_add=True)),
                ('jseekers_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
