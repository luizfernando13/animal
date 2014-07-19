#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('animal.acessos.views',
	url(r'^grupo/$', 'grupo_create', name='grupo_create'),
	url(r'^grupo/(?P<id>\d+)/$', 'grupo_detail', name='grupo_detail'),
	url(r'^grupos_permissoes/(?P<slug>[\w]+)/$', 'grupos_permissoes', name='grupos_permissoes'),
	url(r'^grupos/(?P<slug>[\w\ ]+)/(?P<id_grupo>\d+)/$', 'grupos_add', name='grupos_add'),
	url(r'^grupos/(?P<slug>[\w\ ]+)/(?P<id_grupo>\d+)/remove$', 'grupos_rem', name='grupos_rem'),
	url(r'^permissoes/(?P<slug>[\w\ ]+)/(?P<id_perm>\d+)/$', 'perms_add', name='perms_add'),
	url(r'^permissoes/(?P<slug>[\w\ ]+)/(?P<id_perm>\d+)/remove$', 'perms_rem', name='perms_rem'),

	url(r'^grupo/(?P<grupo_id>\d+)/permissoes/$','grupo_suas_permissoes',name='grupo_suas_permissoes'),
	url(r'^grupo/(?P<grupo_id>\d+)/permissoes/(?P<perm_id>\d+)$','grupos_permissoes_add',name='grupos_permissoes_add'),
	url(r'^grupo/(?P<grupo_id>\d+)/permissoes/(?P<perm_id>\d+)/rem$','grupos_permissoes_rem',name='grupos_permissoes_rem'),

	)
