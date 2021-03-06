"""dataviz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from dataviz import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),

    url(r'^menu/$', views.menu, name='menu'),
    url(r'^analysis/$', views.analysis, name='analysis'),
    url(r'^graph/$', views.graph, name='graph'),

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', auth_views.login, {'template_name': 'dataviz/signin.html'},  name='signin'),
    url(r'^signout/$', auth_views.logout, {'template_name': 'dataviz/signout.html'}, name='signout'),
    url(r'^account_activation_sent/$',
        views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
