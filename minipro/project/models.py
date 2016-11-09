from django.db import models
from taggit.managers import TaggableManager

class login(models.Model):
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=150)
	body = models.TextField()
	created = models.DateTimeField('date only') 
	tags = TaggableManager()

	def __unicode__(self):
		return self.title

class posts(models.Model):
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=150)
	body = models.TextField()
	created = models.DateTimeField('date only') 
	tags = TaggableManager()

	def __unicode__(self):
		return self.title
