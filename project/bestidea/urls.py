from django.conf.urls import patterns, include, url
from bestidea.views import hello
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	('^hello/$',hello),
    url(r'^links/$','bestidea.apps.linkr.views.index_link'),
    url(r'^links/(?P<item_id>\d+)/$','bestidea.apps.linkr.views.detail_link'),
    url(r'^links/new/$','bestidea.apps.linkr.views.new_link'),

    url(r'^topics/$','bestidea.apps.linkr.views.index_topic'),
    url(r'^topics/(?P<topic_id>\d+)/$','bestidea.apps.linkr.views.detail_topic'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
