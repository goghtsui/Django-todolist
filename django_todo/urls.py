"""django_todo URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from todo.views import index, delete, add, complete, filter_index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^delete/(?P<pk>\d+)/$', delete),
    url(r'^complete/(?P<pk>\d+)/$', complete),
    url(r'^add/', add),
    url(r'^(?P<pk>\w+)/$', filter_index),
    url(r'^$', index),
]