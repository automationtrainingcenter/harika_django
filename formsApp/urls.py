from django.conf.urls import url
from formsApp import views
urlpatterns = [
    url(r'^htmlform/$', views.html_form, name='htmlform'),
    url(r'^djangoform/$', views.django_form, name='djangoform'),
    url(r'^modelform/$', views.model_form, name='modelform'),

]
