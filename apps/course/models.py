# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}

		if len(postData['name']) < 5:
			errors = "Name has to be more than 5 characters in length."
		if len(postData['desc']) < 15:
			errors = "Description has to be longer than 15 characters in length."

		return errors


class Courses(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	#allows the user class to inherit the CourseManager class and the function for validation within it. 
	objects = CourseManager()
