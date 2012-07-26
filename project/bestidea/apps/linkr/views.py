from bestidea.apps.linkr.models import Item , Topic
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404

from bestidea.apps.linkr.forms import ItemForm 
from django.template import RequestContext


def index_link(request):
	latest_links_list = Item.objects.all().order_by('-modified')[:5]
	return render_to_response('linkr/links.html', {'latest_links_list': latest_links_list})

def detail_link(request,item_id):
	it = get_object_or_404(Item, pk=item_id)
	return render_to_response('linkr/link.html', {'item': it})

def index_topic(request):
	latest_topics_list = Topic.objects.all().order_by('-modified')[:5]
	return render_to_response('linkr/topics.html', {'latest_topics_list': latest_topics_list})

def detail_topic(request,topic_id):
	p = get_object_or_404(Topic, pk=topic_id)
	return render_to_response('linkr/topic.html', {'topic': p})

def new_link(request):
	if request.method=='POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/links/')
	else:
		form =ItemForm()
	return render_to_response('linkr/link_form.html',{'form':form}, context_instance=RequestContext(request))
