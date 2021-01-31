from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def home(request):
    return render(request,'initial/home.html')

def jobseekersView(request):
    return render(request,"initial/jobseekers.html")

def contactUs(request):
    context={}
    return render(request,"initial/contactus.html")

def employersView(request):
    return render(request,"initial/employers.html")

def huntersView(request):
    return render(request,"initial/headhunters.html")


def jobSignup1(request):
    if request.method=='POST':
#form is instantiation of form class The idea is to access various form properties like #first_name,last_name ,email
        form=jsSignupForm1(request.POST)
        if form.is_valid():
            form1=form.save()
            first_name=form1.first_name
            last_name=form1.last_name
            email=form1.email
            profile=jobseekers.objects.create(user=form1,jseekers_firstname=first_name,
            jseekers_lastname=last_name,
            jseekers_email=email)
#Remember   user includes id,first_name,last_name,email..The idea is put the user detail in the #database
            form1.save()
            jsid=jobseekers.objects.get(user=form1)
            return HttpResponseRedirect(reverse('js_signup2',args=(jsid.slug,)))
    else:
        form=jsSignupForm1()
    return render(request,"jobseekers_signup/signup.html",{"form":form})


def jobSignup2(request,slug1):
    jsSlug=jobseekers.objects.get(slug=slug1)
    if request.method=='POST':
        form=jsSignUpForm2(request.POST,instance=jsSlug)
        if form.is_valid():
            form1=form.save()
            form1.jseekers_mobile=request.POST['jseekers_mobile']
            form1.jseekers_gender=request.POST['jseekers_gender']
            form1.jseekers_location=request.POST['jseekers_location']
            form1.save()
            return HttpResponseRedirect(reverse('js_signup3',args=(jsSlug.slug,)))
    else:
        form=jsSignUpForm2()
    context={"js": jsSlug, "form": form}
    return render(request, "jobseekers_signup/signup.html", context)

#fields = ["jseekers_industry","jseekers_functions","jseekers_workex","jseekers_currentorg","jseekers_currentdesig"]
def jobSignup3(request,slug1):
    jsSlug=jobseekers.objects.get(slug=slug1)
    if reqeust.method=="POST":
        form=jsSignup3Form(request.POST,instance=jsSlug)
        if form.is_valid():
            form1=form.save()
            form1.jseekers_industry=request.POST["jseekers_industry"]
            form1.jseekers_functions=request.POST["jseekers_functions"]
            form1.jseekers_workex=request.POST["jseekers_workex"]
            form1.jseekers_currentorg=request.POST["jseekers_currentorg"]
            form1.jseekers_currentdesig=request.POST["jseekers_currentdesig"]
            form1.save()
            return HttpResponseRedirect(reverse('js_signup4',args=(jsSlug.slug,)))
        else:
            form=jsSignup3Form()
        context={"js":jsSlug,"form": form}
        return render(request,"jobseekers_signup/NEW_signup2.html",context)


def jobsignupView4(request,slug1):
    jsid= jobseekers.objects.get(slug=slug1)
    if request.method=='POST':
        form=jsSign4Form(request.POST,instance=jsid)
        if form.is_valid():
            user=form.save()
            user.jseekers_school = request.POST['jseekers_school']
            user.jseekers_degree = request.POST['jseekers_degree']
            user.jseekers_field_study = request.POST['jseekers_field_study']
            user.save()
            return HttpResponseRedirect(reverse('js_signup5', args=(jsid.slug,)))
    else:
        form = jsSign4Form()

    context = {"js": jsid, "form": form}
    return render(request, "jobseekers_signup/NEW_signup3.html", context)

def jobsignupView5(request,slug1):
    jsSlug=jobseekers.objects.get(slug=slug1)
    if request.method=="POST":
        form=jsSign5Form(request.POST,instance=jsSlug)
        if form.is_valid():
            user=form.save()
        #fields = ["jseekers_achievement","jseekers_passion"]
            user.jseekers_achievement=request.POST['jseekers_achievement']
            user.jseekers_passion=request.POST['jseekers_passion']
            user.save()
            return HttpResponseRedirect(reverse('js_upload', args=(jsSlug.slug,)))
    else:
        form = jsSign5Form()

    context = {"js": jsSlug, "form": form}
    return render(request, "jobseekers_signup/NEW_signup4.html", context)

def model_form_upload(request,slug1):
    jsslug= jobseekers.objects.get(slug=slug1)
    if request.method == "POST":
        form = signupUploadForm(request.POST, instance=jsslug)
        if form.is_valid():
            user = form.save()
            user.jseekers_pic = request.FILES["jseekers_pic"]
            user.save()
            return HttpResponseRedirect(reverse("home"))
            # return HttpResponseRedirect(reverse("js_signup2", args=(js.jseekers_id,)))

    else:
        form = signupUploadForm()

    context = {"js": jsslug, "form": form}
    return render(request, "jobseekers_signup/NEW_upload.html", context)
