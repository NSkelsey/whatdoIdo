from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
import models
from models import Activity, Catergory
from random import choice
from IPython import embed
import re


def home(request):
    cats = ['volunteer', 'outdoors', 'food', 'drink', 'entertain',
            'winter', 'rents']
    resp_dict = models.get_acts_from_cats(cats)
    return render_to_response('home.html', resp_dict,
            RequestContext(request))

def activity(request, cat, act):
    print "not rand"
    query = models.url_to_name(act)
    act = Activity.objects.get(name=query)
    cato = Catergory.objects.get(name=cat)
    qset = Activity.objects.filter(catergories=cato).exclude(id=act.id)
    if len(qset) > 0:
        na = qset.order_by('?')[0]
        na.__setattr__('from_c', cat)
    else:
        na = {'url': '/static/out.html'}
    resp_dict = {'act': act, 'next_act': na}
    return render_to_response('suggestion.html',
            resp_dict,
            RequestContext(request))

def rand_activity(request, cat, act):
    print "rand"
    resp_dict = {}
    act = Activity.objects.get(name=models.url_to_name(act))
    resp_dict['act'] = act
    resp_dict['next_act'] = {'url': '/random'}
    return render_to_response('suggestion.html',
            resp_dict,
            RequestContext(request))


def random(request, last_act=False):
    ref = request.META.get('HTTP_REFERER')
    regx = r'r/(?P<cat>\S+?)/(?P<act>\S+?)$'
    m = re.search(regx, ref)
    if m is None:
        act = Activity.objects.order_by('?')[0]
        url = act.url()
        url = '/r' + url[2:]
    else:
        actname = models.url_to_name(m.groups()[1])
        act = Activity.objects.exclude(name=actname).order_by('?')[0]
        url = act.url()
        url = '/r' + url[2:]
    return HttpResponseRedirect(url)
