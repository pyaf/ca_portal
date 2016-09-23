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

from ca.models import *
from task.models import *
from notice.models import *
from ca.forms import *
from task.forms import *
from ca.backend import PasswordlessAuthBackend
from task.views import send_email

server = "http://www.ca.technex.in/"

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

            if user.is_active:
                login(request,user)
                return redirect('/dashboard')

            else:
                messages.warning(request, "Please Confirm your email before logging in, for email confirmation check your email.", fail_silently=True)
                return redirect('/login')
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

            user.is_active = False #to be True after email confirmation

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
            # SheetUpdate(caprofile)

            #Create task instances
            tasks = Task.objects.all()
            for task in tasks:
                taskInstance = TaskInstance(task = task, ca = caprofile)
                taskInstance.save()

            message = "Welcome to Campus Ambassador Portal of Technex'17"
            UserNotification.objects.create(ca=caprofile,message=message)

            subject = "Email Confirmation for Technex CA Portal"
            confirmationKey = 'Technex' + email + "caportal"
            confirmationKey = str(hash(confirmationKey))

            try:
                key = Key.objects.get(ca = user.caprofile)
                key.confirmationKey = confirmationKey
                key.save()
            except:
                key = Key(ca = user.caprofile, confirmationKey = confirmationKey)
                key.save()

            body = "Please Cick on the following link to Confirm your Technex CA Portal Email.\n\n"
            body += server + "confirmEmail/" + confirmationKey

            if send_email(email, subject, body):
                messages.success(request, 'Confirmation mail sent!, Please check your mail.', fail_silently=True)
                return redirect('/register')
            else:
                message.warning(request, 'Email Confirmation link can\'n be sent please try to register again.', fail_silently=True)
                return render(request,template_name,context)

        else:# already a user.

            messages.warning(request, "email already registered!, Please click on 'forgot password' on login page.", fail_silently=True)
            return render(request,template_name,context)

    else:
        return render(request,template_name,context)

@csrf_exempt
def confirmEmail(request,confirmationKey):
    if request.method == 'GET':
        try:
            key = Key.objects.get(confirmationKey = int(confirmationKey))
            return render(request,"ca/emailConfirm.html")
        except:
            messages.warning(request,'Invalid Url !')
            return redirect('/login')

    elif request.method == "POST":
        post = request.POST
        try:
            key = Key.objects.get(confirmationKey=confirmationKey)
            caprofile = key.ca
            caprofile.user.is_active = True
            caprofile.user.save()
            try:
                user = PasswordlessAuthBackend().authenticate(username=caprofile.user.email)
                user.backend = 'ca.backend.PasswordlessAuthBackend'
                login(request,user)
                return redirect('/dashboard')
            except Exception as e:
                return HttpResponse(e)
        except:
            raise Http404('Not allowed')

def FbLogin(request):
    pass

@login_required(login_url='/login')
def DashboardView(request):
    template_name = 'ca/dashboard.html'
    ca = request.user.caprofile
    try:
        context = context_call(request)
        if ca.firstVisit == False: #Visiting first time, let him explore the dashboard
            context['firstVisit'] = True
            ca.firstVisit = True
            ca.save()
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
