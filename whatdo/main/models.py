from django.db import models

class Catergory(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    title = models.CharField(max_length=120, blank=True)
    name = models.CharField(max_length=200, blank=True,)
    catergories = models.ManyToManyField(Catergory, null=True)
    phone_num = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='acts')
    date = models.DateTimeField(null=True, blank=True)

    def name_to_url(self):
        return self.name.replace(' ', '+')

    def __unicode__(self):
        return self.name

    def url(self):
        s = "/c/%s/%s" % (self.catergories.all()[0], self.name_to_url())
        return s

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

