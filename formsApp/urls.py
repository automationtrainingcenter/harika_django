from django.conf.urls import url
from formsApp import views
urlpatterns = [
    url(r'^htmlform/$', views.html_form, name='htmlform'),
]
