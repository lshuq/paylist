from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^person/(?P<person_name>[^/]+)/$', person_detail, name='person'),
    url(r'^page/(?P<page_name>[^/]+)/$', page_detail, name='page'),
]
