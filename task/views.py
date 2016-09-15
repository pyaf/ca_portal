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
from TechnexUser.models import *
from task.forms import *

@csrf_exempt
def submitDirectorDetail(request):
	response = {}
	if request.method == 'POST':
		post = request.POST
		form = DirectorDetailForm(post)
		if form.is_valid():
			try:
				directorDetail = DirectorDetail.objects.get(ca = request.user.caprofile)
				directorDetail.directorDetail = post.get('directorDetail')
			except:
				directorDetail = DirectorDetail(ca = request.user.caprofile, directorDetail = post.get('directorDetail'))
			taskInstance = TaskInstance.objects.get(task__taskName = 'Director Contact Details', ca = request.user.caprofile)
			taskInstance.status = 100
			directorDetail.save()
			taskInstance.save()
			response['status'] = 'OK'
		else:
			response['status'] = 'Form Not valid'
	else:
		response['status'] = 'Invalid request'
	return JsonResponse(response)


@csrf_exempt
def submitStudentBodyDetail(request):
	response = {}
	if request.method == 'POST':
		post = request.POST
		form = StudentBodyDetailForm(post)
		if form.is_valid():
			try:
				studentBodyDetail = StudentBodyDetail.objects.get(ca = request.user.caprofile)
				studentBodyDetail.studentBodyDetail = post.get('studentBodyDetail')
			except:
				studentBodyDetail = StudentBodyDetail(ca = request.user.caprofile, studentBodyDetail = post.get('studentBodyDetail'))
			taskInstance = TaskInstance.objects.get(task__taskName = 'Student Body Head Details', ca = request.user.caprofile)
			taskInstance.status = 100
			studentBodyDetail.save()
			taskInstance.save()
			response['status'] = 'OK'
		else:
			response['status'] = 'Form Not valid'
	else:
		response['status'] = 'Invalid request'
	return JsonResponse(response)
