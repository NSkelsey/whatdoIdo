from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from models import Activity, Catergory
from IPython import embed

def home(request):
    return render_to_response('home.html', RequestContext(request))


def suggest(request, cat):
    cat = Catergory.objects.get(name=cat)
    embed()
    resp_dict = {'suggestion': 'GO TO COUPES'}
    return render_to_response('suggestion.html', 
            resp_dict,
            RequestContext(request))


def activity(request, cat, act):
    act = Activity.objects.get(name=act)
    resp_dict = {'act': act}
    return render_to_response('suggestion.html',
            resp_dict,
            RequestContext(request))

