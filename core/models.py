from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Description(models.Model):
	name = models.CharField(max_length=100)
	flag = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name


class User(models.Model):
	name = models.CharField(max_length=200)
	desc = models.ForeignKey(Description, null=True)

	def __unicode__(self):
		return self.name