from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import T_Tag
from .models import T_URL
from .models import T_URL_Tag

#from bs4 import BeautifulSoup
from  BeautifulSoup import BeautifulSoup
import requests
import urllib2
#soup = BeautifulSoup(html_doc, 'html.parser')

def updateTagAndShow(request, tag_id):
	if (request.method == 'POST'):
		updatedTag =  str(request.POST['updatedTag'])

		obj = T_Tag.objects.get(TagID=tag_id)
		obj.Tag = updatedTag
		print obj
		obj.save()
	return HttpResponseRedirect('/tags/' + str(tag_id) +'/')

def editTag(request, tag_id):
	tag_list =  T_Tag.objects.filter(TagID=tag_id)

	for tag_row in tag_list:
		Tag = str(tag_row.Tag)
		TagID = int(str(tag_row.TagID))
	
	context = {
		'Tag': Tag,
		'TagID':TagID,
	}
	return render(request, 'bookmark/editTag.html', context)

def insertTagAndShow(request):
	if (request.method == 'POST'):
		newTag =  str(request.POST['newTag'])
		obj = T_Tag.objects.create(Tag=newTag)
		obj.save()
		print obj.TagID
	return HttpResponseRedirect('/tags/' + str(obj.TagID))

def addTag(request):
	context = {}
	return render(request,'bookmark/addTag.html', context)


def showTags(request):
	tag_list =  T_Tag.objects.all()
	context = {
	'tag_list': tag_list,
	}
	return render(request,'bookmark/tags.html', context)

def showTag(request, tag_id):
	tag_list =  T_Tag.objects.filter(TagID=tag_id)
	isNewTag = False
	context = {
	'isNewTag': isNewTag,
	'tag_list': tag_list,
	}
	return render(request,'bookmark/tag.html', context)


def showHome(request):
	
	url_list = T_URL.objects.all()
	tag_list = T_Tag.objects.all()
	url_tag_list = T_URL_Tag.objects.all()
	context = {
		'url_list': url_list,
		'tag_list': tag_list,
		'url_tag_list': url_tag_list,
	}
	return render(request,'bookmark/index.html', context)


def showDetails(request, url_id):
	url_list = T_URL.objects.filter(URLID=url_id)
	url_tag_list = T_URL_Tag.objects.filter(URLID=url_id)
	tag_list = T_Tag.objects.all()
	tags = []
	
	for url_tag_row in url_tag_list:
		for tag_row in tag_list:
			a= int(str(tag_row.TagID))
			b = int(str(url_tag_row.TAGID))
			if( a == b):
				print a, type(a)
				tags.append(str(tag_row.Tag)) 

	url = "abc"
	for url_row in url_list:
		url  = str(url_row.URL)

	urlPage = BeautifulSoup(urllib2.urlopen(url))
	if(urlPage.title == None):
		title = 'No title'
	else:
		title = urlPage.title.string

	tag_list = tags

	context = {
		'url_list': url_list,
		'tag_list': tag_list,
		'title': title,
	}
	return render(request,'bookmark/urldetails.html', context)

