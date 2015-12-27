from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import T_Tag
from .models import T_URL
from .models import T_URL_Tag

"""
# Create your views here.
def index(request):
	return HttpResponse("Minimal Bookmark")
"""
from django.http import HttpResponse


class IndexView(generic.ListView):
	model = T_Tag
	template_name = 'bookmark/index.html'
	context_object_name = 'tag_list'