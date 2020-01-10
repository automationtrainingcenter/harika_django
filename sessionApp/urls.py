from django.conf.urls import url
from sessionApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products/$', views.products_page, name='products'),
    url(r'^cart/$', views.cart_page, name='cart'),
]
