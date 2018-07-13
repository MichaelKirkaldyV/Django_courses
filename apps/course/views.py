# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import *

def index(request):
	context = {
		"courses": Courses.objects.all()
	}
	return render(request, "course/index.html", context)

def add_course(request):
	#sets the post data to variables to be queried. 
	name = request.POST['name']
	desc = request.POST['desc']

	errors = Courses.objects.basic_validator(request.POST)
	#if there is a tag in errors, list them.
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
			return redirect('/')
	else:
		Courses.objects.create(name=name, desc=desc)
		return redirect('/')

def remove(request, id):
	context = {
		"course": Courses.objects.get(id=id)
	}
	return render(request, "course/remove.html", context)

def delete(request, id):
	course1 = Courses.objects.get(id=id)
	course1.delete()
	return redirect('/')
