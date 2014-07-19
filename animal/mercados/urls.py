#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('animal.mercados.views',
    url(r'^anuncio/$', 'anuncio_create', name='anuncio_create'),
    
    url(r'^edit/(?P<id>\d+)/$', 'anuncio_edit', name='anuncio_edit'),
    url(r'^detail/(?P<id>\d+)/$', 'anuncio_detail', name='anuncio_detail'),
    url(r'^$', 'anuncios', name='anuncios'),
    )