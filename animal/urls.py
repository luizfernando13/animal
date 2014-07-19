from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', 'animal.animais.views.home', name='home'),
        url(r'^login/','django.contrib.auth.views.login',{"template_name":'acessos/login.html'}),
        url(r'^logout/','django.contrib.auth.views.logout_then_login',{'login_url': '/'}),
        url(r'^compra_venda/', include('animal.mercados.urls',namespace='mercados')),
        url(r'^animalandros/', include('animal.animais.urls',namespace='animais')),
        url(r'^acesso/', include('animal.acessos.urls',namespace='acessos')),        
        url(r'^admin/', include('admin_honeypot.urls')),
        url(r'^secret/', include(admin.site.urls)),
       
    )

from django.conf import settings
urlpatterns +=patterns('',
    (r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),
)
