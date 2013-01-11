from django.conf.urls import patterns, include, url
from main import views
from whatdo import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^r/(?P<cat>\S+?)/(?P<act>\S+?)$', views.rand_activity),
    url(r'^c/(?P<cat>\S+?)/(?P<act>\S+?)$', views.activity),
    url(r'^random$', views.random),
    url(r'^random?(?P<last_act>\S+?)$', views.random),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
