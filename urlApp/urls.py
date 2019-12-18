from django.conf.urls import url
from urlApp.views import get_time, get_id, get_user, get_user_details

urlpatterns = [
    url(r'^time/$', get_time),
    url(r'^time/(\d+)/$', get_time),
    url(r'^(?P<id>\d+)/$', get_id),
    url(r'^(?P<username>\w+)/$', get_user),
    url(
        r'^(?P<username>\w+)/(?P<id>\d+)/(?P<email>[\w.@-]+)/$', get_user_details),

]
