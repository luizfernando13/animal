from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^login/','django.contrib.auth.views.login',{"template_name":'acessos/login.html'}),
        url(r'^logout/','django.contrib.auth.views.logout_then_login',{'login_url': '/'}),
        
        url(r'^acesso/', include('projeto.acessos.urls',namespace='acessos')),        
        url(r'^admin/', include('admin_honeypot.urls')),
        url(r'^secret/', include(admin.site.urls)),
    )

    ########## ANONIMO ##########

    ########## USUARIO GERAL ##########    
    #home/ Serao exibidos os menus de acordo com suas visoes
    ########## USUARIO ADMINISTRADOR GERAL ##########
    ########## USUARIO DIRETOR RH ##########
    ########## USUARIO GERENTE RH ##########
    ########## USUARIO OPERADOR RH ##########
    ########## USUARIO DIRETOR ACADEMICO ##########
    ########## USUARIO GERENTE ACADEMICO ##########
    ########## USUARIO OPERADOR ACADEMICO ##########
    ########## USUARIO DIRETOR ESTATISTICO ##########
    ########## USUARIO GERENTE ESTATISTICO ##########
    ########## USUARIO OPERADOR ESTATISTISCO ##########
    ########## USUARIO DIRETOR ESCOLAR ##########
    ########## USUARIO GERENTE ESCOLAR ##########
    ########## USUARIO OPERADOR ESCOLAR ##########
    ########## USUARIO PROFESSOR ##########
    ########## USUARIO ALUNO ##########
    ########## USUARIO RESPONSAVEL ##########

    ########## USUARIO BIBLIOTECARIO ##########
    ########## USUARIO ALMOXARIFE ##########



    #/
    #

from django.conf import settings
urlpatterns +=patterns('',
    (r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),
)
