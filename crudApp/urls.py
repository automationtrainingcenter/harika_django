from django.conf.urls import url
from crudApp import views

urlpatterns = [
    url(r'^$', views.getStudents, name='students_list'),
    url(r'^create/$', views.createStudent, name="create"),
    url(r'^update/(?P<id>\d+)/$', views.updateStudent, name='update'),
    url(r'^delete/(?P<id>\d+)/$', views.deleteStudent, name='delete')
]
