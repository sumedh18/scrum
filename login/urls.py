from django.conf.urls import url
from login.views import *

urlpatterns = [
	url(r'^$', main_page),
	
	url(r'^login/$', login),
	url(r'^logout/$', logout),
	]