from django import forms
from .models import jobseekers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm



class jsSignupForm1(UserCreationForm):
    first_name=forms.CharField(label='first_name',max_length=100)
    last_name=forms.CharField(label='last_name',max_length=100)
    email=forms.CharField(label='email')

    class Meta:
        model=User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class jsSignUpForm2(ModelForm):
    class Meta:
        model=jobseekers
        fields=["jseekers_mobile", "jseekers_gender", "jseekers_location"]

class jsSignup3Form(ModelForm):
    class Meta:
        model = jobseekers
        fields = ["jseekers_industry","jseekers_functions","jseekers_workex","jseekers_currentorg","jseekers_currentdesig"]

class jsSign4Form(ModelForm):
    class Meta:
        model = jobseekers
        fields = ["jseekers_school","jseekers_degree","jseekers_field_study"]

class jsSign5Form(ModelForm):
    class Meta:
        model = jobseekers
        fields = ["jseekers_achievement","jseekers_passion"]
        #exclude = ["user"]

class signupUploadForm(ModelForm):
    class Meta:
        model = jobseekers
        fields=["jseekers_pic"]
