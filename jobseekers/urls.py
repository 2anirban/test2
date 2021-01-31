from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.jobSignup1,name='signup'),
    path("signupjs1/<slug:slug1>/", views.jobSignup2,name="js_signup2" ),
    path("signupjs2/<slug:slug1>/", views.jobSignup3,name="js_signup3" ),
    path("signupjs3/<slug:slug1>/", views.jobsignupView4,name="js_signup4" ),
    path("signupjs4/<slug:slug1>/", views.jobsignupView5,name="js_signup5" ),
    path("signupjs5/<slug:slug1>/", views.model_form_upload, name="js_upload"),
    

]
