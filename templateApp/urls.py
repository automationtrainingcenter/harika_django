# template app urls
from django.conf.urls import url
from templateApp import views
urlpatterns = [
    url(r'^home/$', views.template_home, name='template_home'),
    url(r'^data/$', views.template_data, name='template_data'),

]
