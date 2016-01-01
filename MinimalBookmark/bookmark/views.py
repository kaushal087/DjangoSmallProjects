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
"""




def showHome(request):
	
	url_list = T_URL.objects.all()
	tag_list = T_Tag.objects.all()
	url_tag_list = T_URL_Tag.objects.all()
	print url_list
	print tag_list


	context = {
		'url_list': url_list,
		'tag_list': tag_list,
		'url_tag_list': url_tag_list,
	}
	return render(request,'bookmark/index.html', context)
#	return HttpResponse(template.render(context, request))



def showDetails(request, url_id):
	url_list = T_URL.objects.filter(URLID=url_id)
	url_tag_list = T_URL_Tag.objects.filter(URLID=url_id)
	tag_list = T_Tag.objects.all()
	print tag_list
	print url_tag_list

	tags = []
	
	for url_tag_row in url_tag_list:
		for tag_row in tag_list:
			a= int(str(tag_row.TagID))
			b = int(str(url_tag_row.TAGID))
			if( a == b):
				print a, type(a)
				tags.append(str(tag_row.Tag)) 

	print tags
	
	tag_list = tags
	
	context = {
		'url_list': url_list,
		'tag_list': tag_list,
	}
	return render(request,'bookmark/urldetails.html', context)
#	return HttpResponse(template.render(context, request))


"""
def showDetails(request, url_id):
	url_rows = T_URL.objects.get(URLID=url_id)
	template = loader.get_template('bookmark/urldetails.html')
	context = {
		'url_rows': url_rows,
	}
	return HttpResponse(template.render(context, request))
"""
"""
latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
"""
"""
class Show(generic.ListView):
    template_name = 'bookmark/urldetails.html'
    context_object_name = 'url_rows'
    queryset = T_URL.objects.all()
    def get_context_data(self, **kwargs):
		context = super(Show, self).get_context_data(**kwargs)
		context['url_rows'] = T_URL.objects.get(URLID=url_id)
		return context
"""
"""
	def get_queryset(self):
    	return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
"""