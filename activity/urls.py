from django.conf.urls import patterns, url

urlpatterns = patterns('', 
    url(r'^$', 'activity.views.activities'),
    url(r'^search/$', 'activity.views.search'),
    #url(r'^(?P<pk>[-\w]+)/$', 'technique.views.view'),
    #url(r'^(?P<pk>[-\w]+)/edit/$', 'technique.views.create'),
)

