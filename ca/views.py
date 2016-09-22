from django.shortcuts import render, render_to_response, HttpResponse, redirect
from django.http import Http404,JsonResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import requests, json, facebook, re
from ca.forms import *
from ca.models import *
from task.models import *
from task.forms import *

def context_call(request):
    # college = request.user.caprofile.college
    # ca_college_profile = CAProfile.objects.filter(college=college) #for showing other CAs of one's college.

    #will raise an error in  time visit of CA to the dashborad, when the User hasn't  created caprofile
    #using ProfileCreateView and trying to visit dashboard
    try:
        ca = request.user.caprofile
    except:
        ca = None
    taskInstances = TaskInstance.objects.filter(ca = ca)
    try:
        dd = DirectorDetail.objects.get(ca=ca)
        ddData = dd.directorDetail
    except:
        ddData = None
    try:
        sbd = StudentBodyDetail.objects.get(ca=ca)
        sbdData = sbd.studentBodyDetail
    except:
        sbdData = None
    context = {
            # 'technexuser_college_count' : TechProfile.objects.filter(college=college).count(),
            'caprofile' : ca,
            'user_msgs': ca.usernotification_set.filter(mark_read=False),
            'all_user_msgs': ca.usernotification_set.all(),
            'taskInstances' : taskInstances,
            'ddform':DirectorDetailForm(initial={'directorDetail':ddData}),
            'sbdform':StudentBodyDetailForm(initial={'studentBodyDetail' : sbdData}),

            # 'dd_description':Task.objects.get(taskId=1).taskDescription,
            # 'sbd_description':Task.objects.get(taskId=2).taskDescription,
            # 'fb_description':Task.objects.get(taskId=3).taskDescription,
            # 'mass_msgs': ca.massnotification_set.all,
            # 'total_unread_msgs': ca.massnotification_set.all().count() + ca.usernotification_set.filter(mark_read=False).count(),
            # 'tasks' : Task.objects.all(),
            # 'poster_count': ca.poster_set.count(),
            # 'form' : ImageUploadForm(),
            # 'techprofiles' : TechProfile.objects.filter(college=college),
            # 'posters' : Poster.objects.filter(ca=request.user.caprofile),


        }
    # print context['tasks']
    return context

def SheetUpdate(caprofile):
    dic = {
    'name' : caprofile.user.first_name,
    'email' : caprofile.user.email,
    'college' : caprofile.college,
    'year' : caprofile.year,
    'mobileNumber': caprofile.mobile_number,
    'whatsappNumber': caprofile.whatsapp_number,
    'postalAddress' : caprofile.postal_address,
    'pincode': caprofile.pinCode,
    'whyChooseYou': caprofile.whyChooseYou,
    'pastExp':caprofile.pastExp,
    }

    url = 'https://script.google.com/macros/s/AKfycbzEw71pbzcam4W2Jh9-bExZU7Ocv_fBULgmZBf7rMSxwdrHYY0/exec'
    requests.post(url,data=dic)

class IndexView(generic.View):
    def get(self, request):
        # template_name = 'ca/index.html'

        # return render(request, template_name, {})
        return redirect('http://technex.in/ca')

def LoginView(request):
    template_name = 'ca/login.html'
    if request.method == "POST":
        post = request.POST
        email = post['email']
        password = post['password']
        user = authenticate(username=email, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
            # return render(request,'ca/thanks.html'{})
        else:
            messages.error(request,'Invalid Credentials',fail_silently=True)
            return render(request,template_name,{})
    else:
        return render(request,template_name,{})


def CARegistrationView(request):
    template_name = 'ca/register.html'
    context = {
            'all_colleges':College.objects.all(),
    }
    if request.method == "POST":
        post = request.POST
        email = post['form-email']
        password1 = post['form-password']
        try:
            already_a_user = User.objects.get(username=email)
        except:# unique user.
            already_a_user = False

        if not already_a_user:#create new User instance.
            user = User.objects.create_user(username=email,email=email)
            user.first_name = post.get('form-first-name')
            user.set_password(password1)
            user.save()

            caprofile = CAProfile.objects.create(user=user)
            try:
                college = College.objects.get(collegeName=post.get('form-college'))
            except:
                college = College.objects.create(collegeName=post.get('form-college'))

            caprofile.college = college
            caprofile.year = post.get('year')
            caprofile.mobile_number = post.get('form-mobilenumber')
            caprofile.whatsapp_number = post.get('form-whatsapp')
            caprofile.postal_address = post.get('form-address')
            caprofile.pinCode = post.get('form-pincode')
            caprofile.whyChooseYou = post.get('form-choose')
            caprofile.pastExp = post.get('form-experiences')
            caprofile.save()
            SheetUpdate(caprofile)
            tasks = Task.objects.all()
            for task in tasks:
                taskInstance = TaskInstance(task = task, ca = caprofile)
                taskInstance.save()
            # UserNotification.objects.create(ca=caprofile,message)
            new_user = authenticate(username=email,password=password1)
            login(request,new_user)

            return redirect('/dashboard')
            # return render(request,'ca/dashboard.html',{})
        else:# already a user.

            messages.warning(request,'email already registered!, if you have already registered for Technex, the link of CA registration is at dashboard',fail_silently=True)
            return render(request,template_name,context)


    else:
        return render(request,template_name,context)


def FbLogin(request):
    pass

@login_required(login_url='/login')
def DashboardView(request):
    template_name = 'ca/dashboard.html'
    try:
        context = context_call(request)
        return render(request,template_name,context)
    except Exception as e:
        return HttpResponse(e)

@login_required(login_url = "/login")
def AccountDetailView(request):
    template_name = 'ca/settings.html'
    ca = request.user.caprofile
    context = context_call(request)
    data = {
        'name': request.user.first_name,
        'year': ca.year,
        'mobile_number' : ca.mobile_number,
        'whatsapp_number' : ca.whatsapp_number,
        'postal_address' : ca.postal_address,
        'pincode' : ca.pinCode
    }
    context['profileForm'] = ProfileUpdateForm(initial=data)
    if request.method == "POST":
        post = request.POST
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            request.user.first_name = post.get('name')
            request.user.save()
            ca.year = post.get('year')
            ca.mobile_number = post.get('mobile_number')
            ca.whatsapp_number = post.get('whatsapp_number')
            ca.postal_address = post.get('postal_address')
            ca.pinCode = post.get('pincode')
            ca.save()
            messages.success(request,'Profile updated successfully!',fail_silently=True)
            return redirect('/settings')
        else:
            messages.warning(request,'Invalid input!',fail_silently=True)


    return render(request, template_name, context)




@login_required(login_url = "/login")
def PasswordChangeView(request):
    template_name = 'ca/passwordChange.html'
    context = {
        'form':PasswordChangeForm(),
    }
    if request.method == 'POST':
        post = request.POST
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            oldPassword = post.get('oldPassword')
            password1 = post.get('password1')
            password2 = post.get('password2')
            if password1 == password2 :
                user = authenticate(username=request.user.email,password=oldPassword)
                print user,oldPassword
                if user is not None:
                    request.user.set_password(password1)
                    request.user.save()
                    user = authenticate(username=request.user.email,password=password1)
                    login(request,user)
                    messages.success(request,'Password successfully set!',fail_silently=True)
                    return redirect('/dashboard')
                else:
                    messages.warning(request,'Wrong old password!',fail_silently=True)
                    return redirect('/passwordChange')

            else:
                messages.warning(request,"Passwords didn't match!!",fail_silently=True)
                return redirect('/passwordChange')
    else:
        return render(request, template_name, context)



@login_required(login_url = "/login")
def LogoutView(request):
    logout(request)
    return redirect('/')
