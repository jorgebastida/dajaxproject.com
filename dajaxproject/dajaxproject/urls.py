from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .examples import views as examples_views
dajaxice_autodiscover()

urlpatterns = patterns('',

    # dajax examples
    url(r'^multiply/$', examples_views.MultiplyExample.as_view(), name='dajax-multiply-example'),
    url(r'^maps/$', examples_views.MapsExample.as_view(), name='example-maps'),
    url(r'^random/$', examples_views.RandomExample.as_view(), name='example-random'),
    url(r'^forms/$', examples_views.FormExample.as_view(), name='example-forms'),
    url(r'^flickr/$', examples_views.FlickrExample.as_view(), name='example-flickr'),
    url(r'^fullform/$', 'examples.views.full_form_example', name='example-fullform'),
    url(r'^pagination/$', 'examples.views.pagination_example', name='example-pagination'),

    # dajaxice examples
    url(r'^dajaxice/$', examples_views.DajaxiceExample.as_view(), name='dajaxice-example'),
    url(r'^dajaxice-args/$', examples_views.DajaxiceArgsExample.as_view(), name='dajaxice-args-example'),

    # Index
    url(r'^$', examples_views.Index.as_view(), name='index'),

    # Dajaxice
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()
