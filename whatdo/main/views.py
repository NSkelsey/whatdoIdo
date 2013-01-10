from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
import models
from models import Activity, Catergory
from random import choice
from IPython import embed

def home(request):
    cats = ['volunteer', 'outdoors', 'food', 'drink', 'entertain',
            'winter', 'rents']
    resp_dict = models.get_acts_from_cats(cats)
    rand = Activity.objects.filter().order_by('?')[0]
    resp_dict['rand'] = rand
    return render_to_response('home.html', resp_dict,
            RequestContext(request))

def activity(request, cat, act):
    print 'activity'
    query = models.url_to_name(act)
    act = Activity.objects.get(name=query)
    na = models.pull_from_act(cat)
    resp_dict = {'act': act, 'next_act': na}
    return render_to_response('suggestion.html',
            resp_dict,
            RequestContext(request))

