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


"""
class IndexView(generic.ListView):
	model = T_URL
	template_name = 'bookmark/index.html'
	context_object_name = 'url_list'
	"""
"""
class IndexView(ListView):
context_object_name = 'home_list'    
template_name = 'contacts/index.html'
queryset = Individual.objects.all()

def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['roles'] = Role.objects.all()
    context['venue_list'] = Venue.objects.all()
    context['festival_list'] = Festival.objects.all()
    # And so on for more models
        return context

"""
class IndexView(generic.ListView):
	context_object_name = 'url_tag_list'    
	template_name = 'bookmark/index.html'
	queryset = T_URL_Tag.objects.all()

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['url_list'] = T_URL.objects.all()
		context['tag_list'] = T_Tag.objects.all()
		return context
