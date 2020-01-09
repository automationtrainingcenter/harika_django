from django.conf.urls import url, include
from crudApp import views

urlpatterns = [
    url(r'^$', views.getStudents, name='students_list'),
    url(r'^create/$', views.createStudent, name="create"),
    url(r'^update/(?P<id>\d+)/$', views.updateStudent, name='update'),
    url(r'^delete/(?P<id>\d+)/$', views.deleteStudent, name='delete'),
    url(r'^logout/$', views.logout),
    # class based views urls
    url(r'^cbv/$', views.StudentListView.as_view(), name='cbv_student_list'),
    url(r'^cbv/(?P<pk>\d+)/$', views.StudentDetailView.as_view(),
        name='cbv_student_detail'),
    url(r'^cbv/create', views.StudentCreateView.as_view(), name='cbv_create'),
    url(r'^cbv/update/(?P<pk>\d+)$',
        views.StudentUpdateView.as_view(), name='cbv_update'),
    url(r'^cbv/delete/(?P<pk>\d+)$',
        views.StudentDeleteView.as_view(), name='cbv_delete')
]
