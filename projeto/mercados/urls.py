#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('projeto.mercados.views',
    url(r'^anuncio/$', 'anuncio_create', name='anuncio_create'),
    )