from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'homePage'),
    url(r'^profile/$', views.profile, name='userProfile'),
    url(r'^search/$', views.search_user, name='locateUser'),
]