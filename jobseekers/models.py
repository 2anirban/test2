from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .utils import *

class jobseekers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    jseekers_id = models.AutoField(primary_key=True)
    jseekers_firstname = models.CharField(max_length=200, blank=True, null=True)
    jseekers_lastname = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=250,unique=True)
    jseekers_email = models.EmailField(blank=True, null=True)
    jseekers_password = models.CharField(max_length=200, blank=True, null=True)
    jseekers_pic = models.ImageField(upload_to="static/profilepics", blank=True, null=True)
    jseekers_headline = models.CharField(max_length=4000, blank=True, null=True)
    jseekers_mobile = models.CharField(max_length=15, blank=True, null=True)
    gender_type = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    jseekers_gender = models.CharField(max_length=200, choices=gender_type, blank=True, null=True)
    jseekers_location = models.CharField(max_length=200, blank=True, null=True)
    jseekers_otherinfo = models.CharField(max_length=2000, blank=True, null=True)
    # professional detail
    industry_type = (
        ("Select", "Select"),
        ("Construction / Engineering / Cement / Metals", "Construction / Engineering / Cement / Metals"),
        ("Consumer Durables", "Consumer Durables"),
        ("FMCG/Food/Beverages", "FMCG/Food/Beverages"),
        ("IT Software", "IT Software"),
        ("IT Hardware", "IT Hardware"),
        ("KPO/Research & Analytics", "KPO/Research & Analytics"),
        ("Internet/Ecommerce", "Internet/Ecommerce"),
        ("BPO", "BPO"),
        ("Strategy /Management Consulting", "Strategy /Management Consulting"),
        ("Textiles / Garments / Accessories", "Textiles / Garments / Accessories"),
        ("Information Technology", "Information Technology"),
        ("Software Application/Web Development", "Software Application/Web Development"),
        ("Accounts", "Accounts"),
        ("Medical& Healthcare", "Medical& Healthcare"),
    )
    jseekers_industry = models.CharField(max_length=200, choices=industry_type, blank=True, null=True)
    functions_type = (
        ("Select", "Select"),
        ("Accounting / Tax / Company Secretary / Audit", "Accounting / Tax / Company Secretary / Audit"),
        ("Analytics & Business Intelligence", "Analytics & Business Intelligence"),
        ("Corporate Planning / Consulting / Strategy", "Corporate Planning / Consulting / Strategy"),
        ("Entrepreneur / Businessman / Outside Management Consultant",
         "Entrepreneur / Businessman / Outside Management Consultant"),
        ("HR / Admin / PM / IR / Training", "HR / Admin / PM / IR / Training"),
        ("ITES / BPO / Operations", "ITES / BPO / Operations"),
        ("Medical Professional / Healthcare Practitioner / Technician",
         "Medical Professional / Healthcare Practitioner / Technician"),
        ("Mktg / Advtg  Media Planning / PR / Corp. Comm", "Mktg / Advtg  Media Planning / PR / Corp. Comm"),
        ("R&D / Engineering Design", "R&D / Engineering Design"),
        ("Sales / Business Development / Client Servicing", "Sales / Business Development / Client Servicing"),
        ("Software Development - ALL", "Software Development - ALL"),
        ("Software Development - Application Programming", "Software Development - Application Programming"),
        ("Software Development - e-commerce / Internet Technologies",
         "Software Development - e-commerce / Internet Technologies"),
        ("Software Development - Database Administration", "Software Development - Database Administration"),
        ("Software Development - Embedded Technologies", "Software Development - Embedded Technologies"),
        ("Software Development - ERP / CRM", "Software Development - ERP / CRM"),
        ("Top Management", "Top Management"),
        ("Others", "Others"),
        ("Customer Relation Management", "Customer Relation Management"),
        ("Finance & Accounting Operations", "Finance & Accounting Operations"),
    )
    jseekers_functions = models.CharField(max_length=200, choices=functions_type, blank=True, null=True)
    jseekers_workex = models.IntegerField( blank=True, null=True)
    jseekers_currentorg = models.CharField(max_length=200, blank=True, null=True)
    jseekers_currentdesig = models.CharField(max_length=200, blank=True, null=True)
    jseekers_currentcv = models.FileField(upload_to="media/cv", blank=True, null=True)
    # previous Jobs
    jseekers_prev_industry = models.CharField(max_length=200, choices=industry_type, blank=True, null=True)
    jseekers_prev_functions = models.CharField(max_length=200, choices=functions_type, blank=True, null=True)
    jseekers_prev_org = models.CharField(max_length=200, blank=True, null=True)
    jseekers_prev_desig = models.CharField(max_length=200, blank=True, null=True)
    jseekers_prev_responsibilities = models.CharField(max_length=200, blank=True, null=True)
    jseekers_prev_joiningdate = models.DateField(max_length=50, blank=True, null=True)
    jseekers_prev_relievingdate = models.DateField(max_length=50, blank=True, null=True)
    jseekers_prev_summary = models.CharField(max_length=200, blank=True, null=True)
    # Educational Detail:
    jseekers_school = models.CharField(max_length=200, blank=True, null=True)
    jseekers_degree = models.CharField(max_length=200, blank=True, null=True)
    jseekers_datesattended = models.DateField(max_length=200, blank=True, null=True)
    jseekers_field_study = models.CharField(max_length=200, blank=True, null=True)
    # other Info
    jseekers_achievement = models.CharField(max_length=2000, blank=True, null=True)
    jseekers_passion = models.CharField(max_length=4000, blank=True, null=True)
    jseekers_timestamp = models.DateTimeField(auto_now_add=True)
    jseekers_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)+""+str(self.jseekers_id)

#Writing a function on slug
def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=jobseekers)
