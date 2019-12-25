from django.conf.urls import url
from modelApp import views
urlpatterns = [
    url(r'^programmers/$', views.programmer_list, name='programmers'),
    url(r'^(?P<name>\w+)/info$', views.project_info, name='project_info')
]
