from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^singin/$', views.singUp, name='singIn'),
    url(r'^singup/$', views.singUp, name='singIn'),
]
