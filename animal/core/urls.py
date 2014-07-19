#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('animal.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^config/$', 'config', name='config'),    
    url(r'^home/$', 'home', name='home'),
    url(r'^home2/$', 'homepage2', name='homepage2'),
)