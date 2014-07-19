#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('projeto.animais.views',
    url(r'^novo/$', 'animal_create', name='animal_create'),
    url(r'^lista/$', 'animals', name='animals'),
    url(r'^edit/(?P<id>\d+)/$', 'animal_edit', name='animal_edit'),
    url(r'^detail/(?P<id>\d+)/$', 'animal_detail', name='animal_detail'),
    )