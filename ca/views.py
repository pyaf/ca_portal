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
import requests
import json
import facebook
import re
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
            'mass_msgs': ca.massnotification_set.all,
            'user_msgs': ca.usernotification_set.filter(mark_read=False),
            'all_user_msgs': ca.usernotification_set.all(),
            'total_msgs': ca.massnotification_set.count() + ca.usernotification_set.filter(mark_read=False).count(),
            'tasks' : Task.objects.all(),
            'taskInstances' : taskInstances,
            'ddform':DirectorDetailForm(initial={'directorDetail':ddData}),
            'sbdform':StudentBodyDetailForm(initial={'studentBodyDetail' : sbdData}),

            # 'poster_count': ca.poster_set.count(),
            # 'form' : ImageUploadForm(),
            # 'techprofiles' : TechProfile.objects.filter(college=college),
            # 'posters' : Poster.objects.filter(ca=request.user.caprofile),


        }
    # print context['tasks']
    return context

def LoginView(request):
    template_name = 'ca/login.html'
    context = {}
    return render(request,template_name,context)


class IndexView(generic.View):
    def get(self, request):
        template_name = 'ca/index.html'
        return render(request, template_name, {})

def CARegistrationView(request):
    template_name = 'ca/register.html'
    context = {
            'all_colleges':College.objects.all(),
    }
    if request.method == "POST":
        post = request.POST
        email = post['email']
        password1 = post['password1']
        try:
            already_a_user = User.objects.get(username=email)
        except:# unique user.
            already_a_user = False

        if not already_a_user:#create new User instance.
            user = User.objects.create_user(username=email,email=email)
            user.first_name = post.get('name')
            user.set_password(password1)
            user.save()

            caprofile = CAProfile.objects.create(user=user)
            try:
                college = College.objects.get(collegeName=post.get('college'))
            except:
                college = College.objects.create(collegeName=post.get('college'))

            caprofile.college = college
            caprofile.year = post.get('year')
            caprofile.mobile_number = post.get('mobile_number')
            caprofile.whatsapp_number = post.get('whatsapp_number')
            caprofile.postal_address = post.get('postal_address')
            caprofile.save()
            tasks = Task.objects.all()
            for task in tasks:
                taskInstance = TaskInstance(task = task, ca = caprofile)
                taskInstance.save()
            new_user = authenticate(username=email,password=password1)
            login(request,new_user)

            return redirect('/ca/dashboard')
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
    context = context_call(request)
    return render(request, template_name, context)
