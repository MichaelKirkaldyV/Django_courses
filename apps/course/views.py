# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import *

def index(request):
	context = {
		"courses": Courses.objects.all()
	}
	return render(request, "course/index.html", context)
