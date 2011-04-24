from django.conf import settings
from django.conf.urls.defaults import include, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover                                                                                                            


dajaxice_autodiscover()

urlpatterns = patterns('',
    # Dajaxice
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

    # api
    #(r'^api/v(\d+)/options/?$', 'sipwping.api.options'),

    # index
    (r'', 'sipwping.views.index'),
)

urlpatterns += staticfiles_urlpatterns()

