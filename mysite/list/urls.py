from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', money_list),
    url(r'search/', search_list),
    url(r'searched/', searched_list),
    url(r'list_day/', list_day),
    url(r'list_week/', list_week),
    url(r'list_month/', list_month),
    url(r'^moneylist/(?P<mylist>[^/]+)/$', list_detail, name='moneylist'),
]
