from django.db import models
import urllib

class Catergory(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    title = models.CharField(max_length=120, blank=True)
    name = models.CharField(max_length=200, blank=True,)
    catergories = models.ManyToManyField(Catergory, null=True)
    phone_num = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='acts')
    date = models.DateTimeField(null=True, blank=True)
    date_writeup = models.CharField(max_length=400,blank=True)
    ex_url = models.URLField(blank=True, null=True)

    def name_to_url(self):
        return self.name.replace(' ', '+')

    def __unicode__(self):
        return self.name

    def url(self):
        cat = self.catergories.all()[0]
        try:
            cat = self.from_c
        except AttributeError:
            pass
        s = "/c/%s/%s" % (cat, self.name_to_url())
        return s

    def make_static_map(self):
        if self.address is None:
            return None
        addr = urllib.quote(self.address)
        gmap = "http://maps.googleapis.com/maps/api/staticmap?&size=400x400&sensor=false&markers=color:green|%s&markers=color:orange|1826,University,Avenue,Charlottesville,VA,22904" % addr
        return gmap

    def get_ex_url(self):
        if not self.ex_url:
            return self.url()
        return self.ex_url

def url_to_name(url):
    return url.replace('+', ' ')

def pull_from_act(query):
    act = Activity.objects.filter(catergories=Catergory.objects.get(name=query)).order_by('?')[0]
    return act

def get_acts_from_cats(lst):
    resp_d = {}
    for cat in lst:
        act = pull_from_act(cat)
        resp_d[cat] = act
    return resp_d

