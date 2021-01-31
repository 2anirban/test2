
from django.contrib import admin
from django.urls import path,include
from jobseekers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('jobseekers',views.jobseekersView,name='jobseekers'),
    path('employers',views.employersView,name='employers'),
    path('hunters',views.huntersView,name='hunters'),
    path('contactus',views.contactUs,name='contactus'),
    path('jobseekers/',include('jobseekers.urls')),

]
