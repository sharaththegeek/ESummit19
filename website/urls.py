from django.conf.urls import url
from . import views
from views import home
from views import login
from views import trylog

urlpatterns = [
   url(r'^$',home),
   url(r'^login/',login),
   url(r'^trylog/',trylog),
]