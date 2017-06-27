from django.conf.urls import url
from .views import logout, profile, login

urlpatterns = [
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login', login, name='login'),
]