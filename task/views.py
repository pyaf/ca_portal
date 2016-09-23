from django.shortcuts import render, render_to_response, HttpResponse, redirect
from django.http import Http404, JsonResponse
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
server = "http://www.ca.technex.in/"
@csrf_exempt
def submitDirectorDetail(request):
	response = {}
	if request.method == 'POST':
		post = request.POST
		form = DirectorDetailForm(post)
		dd = post.get('directorDetail')
		try:
			directorDetail = DirectorDetail.objects.get(ca = request.user.caprofile)
			directorDetail.directorDetail = dd
		except:
			directorDetail = DirectorDetail(ca = request.user.caprofile, directorDetail = dd)
		taskInstance = TaskInstance.objects.get(task__taskName = 'Director Contact Details', ca = request.user.caprofile)

		if dd == '':
			taskInstance.status = 0
		else:
			taskInstance.status = 100

		directorDetail.save()
		taskInstance.save()
		response['status'] = 'OK'
	else:
		response['status'] = 'Invalid request'
	return JsonResponse(response)


@csrf_exempt
def submitStudentBodyDetail(request):
	response = {}
	if request.method == 'POST':
		post = request.POST
		form = StudentBodyDetailForm(post)
		ca = request.user.caprofile
		sbd = post.get('studentBodyDetail')
		try:
			studentBodyDetail = StudentBodyDetail.objects.get(ca = ca)
			studentBodyDetail.studentBodyDetail = sbd
		except:
			studentBodyDetail = StudentBodyDetail(ca = ca, studentBodyDetail = sbd)
		taskInstance = TaskInstance.objects.get(task__taskName = 'Student Body Head Details', ca = ca)

		if sbd == '':
			taskInstance.status = 0
		else:
			taskInstance.status = 100

		studentBodyDetail.save()
		taskInstance.save()
		response['status'] = 'OK'

	else:
		response['status'] = 'Invalid request'
	return JsonResponse(response)

@login_required(login_url = "/login")
def AllPosterView(request):
    template_name = 'ca/all_posters.html'
    context = context_call(request)
    return render(request,template_name, context)

@login_required(login_url = "/login")
def ToDoListView(request):
    template_name = 'ca/to_do_list.html'
    context = context_call(request)
    return render(request,template_name,context)


@login_required(login_url='/login')
def UpcomingEventsView(request):
    template_name = 'ca/upcoming_events.html'
    context = context_call(request)

    return render(request,template_name,context)


@login_required(login_url = "/login")
def PosterUploadView(request):
    template_name = 'ca/poster_form.html'
    context = context_call(request)

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            img.save()
            messages.success(request, 'Poster uploaded successfully.',fail_silently=True)
            return redirect('/ca/dashboard/')
        else:
            return render(request,template_name,context)
    else:
        return render(request,template_name,context)


'''
Auto like,comment and share of posts of technex page while checking if post already shared.
limit for sharing number of posts arranged as per the latest.
'''
def auto_likes(request,limit = 2):
    token="EAAGjmqGLNv0BAARPYwZBPZAWBZBeDcSFlUCRNJOFRM83P0qNG1y4BZBFZBH8VME0uBarCpeRLmTW8Y4Qn7Ef4KCLnqBDR531FA3vyAEIXYmvhIsUJNR1sq0RHlJA4kDGZCLw8iBLiCZCOrRAE6L4BU7ZCvkaZB4QDn22x14bbAA0RIgZDZD"
    graph = facebook.GraphAPI(access_token = token, version= '2.1')
    profile = graph.get_object(id ='225615937462895')
    posts = graph.get_connections(profile['id'],"posts",limit = limit)
    userPosts = graph.get_object("me/feed")
    #print(userPosts['data'])

    links = []
    for userPost in userPosts['data']:
        links.append(userPost['link'])
    #postIds = []
    linksPosted = []
    for post in posts['data']:
        try:
            graph.put_object(post['id'],"likes")
            #postIds.append(post['link'])
            attachment = {
            'link':post['link'],
            'name': 'testName',
            'caption':'testCaption',
            'description':'testDescription',
            'picture':''
            }
            print post['link']
            if post['link'] not in links:
                linksPosted.append(post['link'])
                graph.put_wall_post(message='',attachment = attachment)
            #graph.put_comment(post['id'],message="(Y)")
        except:
            continue
    return HttpResponse(str(linksPosted))

#if user likes the page widout the bug :)
def user_likes_page(page_id, token):
    """
    Returns whether a user likes a page
    """
    url = 'https://graph.facebook.com/me/likes/%s/' % page_id
    parameters = {'access_token': token}
    r = requests.get(url, params = parameters)
    result = json.loads(r.text)
    print r.text
    if result['data']:
        return True
    else:
        return False

def demoCheck(request):
    pageId = '225615937462895'
    token= request.GET['access_token']#"EAAGjmqGLNv0BAARPYwZBPZAWBZBeDcSFlUCRNJOFRM83P0qNG1y4BZBFZBH8VME0uBarCpeRLmTW8Y4Qn7Ef4KCLnqBDR531FA3vyAEIXYmvhIsUJNR1sq0RHlJA4kDGZCLw8iBLiCZCOrRAE6L4BU7ZCvkaZB4QDn22x14bbAA0RIgZDZD"
    if user_likes_page(pageId,token):
        return HttpResponse("liked")
    else:
        return HttpResponse("Not Liked!")

def get_fb_token(app_id, app_secret):
    payload = {'grant_type': 'client_credentials', 'scope':'user_likes,publish_actions', 'client_id': app_id, 'client_secret': app_secret,'redirect_uri':'http://localhost:8000/'}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    print file.text #to test what the FB api responded with
    #result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return file.text

def demofb_id(request):
    print str(request)
    app_id = '461359507257085'
    app_secret = '7be92fe7ee2c2d12cd2351d2a2c0dbb8'
    #token = get_fb_token(app_id, app_secret)
    #facebook.auth_url(app_id,'http://locahost:8000/ca/demofb_id',)
    return render(request,'ca/fblogin.html')

@login_required(login_url = "/login")
@csrf_exempt
def fbConnect(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        try:
            fb_connect = FbConnect.objects.get(ca = request.user.caprofile)
            fb_connect.accessToken = post['accessToken']
            response['status'] = 'updated'
        except:
            fb_connect = FbConnect(ca = request.user.caprofile, accessToken = post['accessToken'], uid = post['uid'])
            response['status'] = 'connected'
        fb_connect.save()
        taskInstance = TaskInstance.objects.get(task__taskName = 'facebook connect', ca = request.user.caprofile)
        taskInstance.status = 100
        taskInstance.save()
        return JsonResponse(response)


def send_email(recipient, subject, body):
    
    return requests.post(
        "https://api.mailgun.net/v3/mg.technex.in/messages",
        auth=("api", "key-cf7f06e72c36031b0097128c90ee896a"),
        data={"from": "No-reply <mailgun@mg.technex.in>",
              "to": recipient,
              "subject": subject,
              "text": body})
@csrf_exempt
def forgotPassword(request):
    if request.method == 'POST':
        post = request.POST
        email = post.get("form-email")
        subject = "Reset Password"
        key = 'Technex'+email+"caportal"
        key = str(hash(key))
        try:
            user = User.objects.get(email = email)

        except:
            messages.warning(request,"Invalid Email!")
            return redirect('/login')
        try:
            forgotPass = ForgotPass.objects.get(ca = user.caprofile)
            forgotPass.key = key
            forgotPass.save()
        except:
            forgotPass = ForgotPass(ca= user.caprofile,key = key)
            forgotPass.save()
        body = "Please Cick on the following link to reset your Password.\n\n"
        body += server+"resetPass/"+key
        if send_email(email,subject,body):
            messages.success(request, "Password Reset link sent to your Email.")
            return redirect('/login')
        else:
            messages.warning(request, "Email couldn't  be send !!")

@csrf_exempt
def resetPass(request,key):
    if request.method == 'GET':

        if True:
            forgotPass = ForgotPass.objects.get(key = int(key))
            print key
            return render(request,"ca/reset.html")
        else:
            messages.warning(request,'Invalid Url !')
            return redirect('/login')

    elif request.method == "POST":
        post = request.POST
        try:
            forgotPass = ForgotPass.objects.get(key=key)
            caprofile = forgotPass.ca
            password1 = post.get('form-password')
            password2 = post.get('form-repeat-password')
            if password1 == password2:
                forgotPass.delete()
                caprofile.user.set_password(password1)
                caprofile.user.save()
                messages.success(request,'password set successfully!',fail_silently=True)
                return redirect('/login')
            else:
                messages.warning(request,"passwords didn't match!")
                url = server+"/resetPass/"+key
                return redirect(request,url)
        except:
            raise Http404('Not allowed')


        return redirect('/resetPass/'+key)
