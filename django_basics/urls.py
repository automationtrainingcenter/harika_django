"""django_basics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from hello.views import index
from crudApp.views import logout
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^urlapp/', include('urlApp.urls')),
    url(r'^templateApp/', include('templateApp.urls')),
    url(r'^modelApp/', include('modelApp.urls')),
    url(r'^formsApp/', include('formsApp.urls')),
    url(r'^crudApp/', include('crudApp.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^sessionApp/', include('sessionApp.urls')),

]
