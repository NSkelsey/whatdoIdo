from django.db import models

class Catergory(models.Model):
    name = models.CharField(max_length=120)
    #activities = models.ManyToManyField('Activity', required=False)

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    title = models.CharField(max_length=120)
    name = models.CharField(max_length=200)
    catergories = models.ManyToManyField(Catergory)
    phone_num = models.IntegerField(blank=False)
    address = models.CharField(max_length=1000, blank=False)

    def name_to_url(self):
        return self.name.replace(' ', '+')

    def __unicode__(self):
        return self.name


