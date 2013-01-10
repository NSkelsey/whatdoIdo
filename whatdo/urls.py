from django.conf.urls import patterns, include, url
from main import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^c/(?P<cat>\S+?)/(?P<act>\S+?)$', views.activity),
    #url(r'^c/(?P<cat>\S+?)$', views.suggest),
    # url(r'^$', 'whatdo1.views.home', name='home'),
    # url(r'^whatdo1/', include('whatdo1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
