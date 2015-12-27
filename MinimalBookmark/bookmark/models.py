from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

@python_2_unicode_compatible
class T_URL(models.Model):
	URLID= models.AutoField(primary_key=True)
	URL = models.CharField(max_length=1000)
	def __str__(self):
		return str(self.URLID)


@python_2_unicode_compatible
class T_Tag(models.Model):
	TagID = models.AutoField(primary_key=True)
	Tag = models.CharField(max_length=100)
	def __str__(self):
		return str(self.TagID)


@python_2_unicode_compatible
class T_URL_Tag(models.Model):
	URLID = models.ForeignKey(T_URL, on_delete=models.CASCADE)
	TAGID = models.ForeignKey(T_Tag, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.URLID)

