# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group,User,Permission
from projeto.acessos.forms import GrupoForm

from django.core.urlresolvers import reverse as r
# Create your views here.


def acesso(request):
	'''
		@acesso: View para vizualizar todos os grupos e permissoes
	'''
	return render(request,'acessos/acesso.html')

def grupos_permissoes(request,slug):
	'''
		@grupos:View que exibe todos os grupos que podem ser inseridos há um determinado user
	'''
	user = User.objects.get(username=slug)	
	#permissoes que o usuario possui
	permissoes_dentro = user.user_permissions.all()
	#permissoes que o usuario nao possui
	permissoes_fora = Permission.objects.exclude(name__startswith='can').exclude(id__in=user.user_permissions.all())	
	return render(request,'acessos/usuario_groups_permissions.html',
		{
			'grupos_dentro':user.groups.all(),
			'grupos_fora':Group.objects.all().exclude(id__in=user.groups.all()),
			'permissoes_fora':permissoes_fora,
			'permissoes_dentro':permissoes_dentro,
			'user':user
		}
		)

def grupos_add(request,slug,id_grupo):
	'''
		@grupos_add: View para adicionar grupo de um determinado user
	'''
	obj = User.objects.get(username=slug)
	gru = Group.objects.get(id=id_grupo)
	obj.groups.add(gru)
	return HttpResponseRedirect(r('acessos:grupos_permissoes', args=[obj.get_absolute_url().split('/')[2]]))

def grupos_rem(request,slug,id_grupo):
	'''
		@grupos_rem: View para remover grupo de um determinado user
	'''
	obj = User.objects.get(username=slug)
	gru = Group.objects.get(id=id_grupo)
	obj.groups.remove(gru)
	return HttpResponseRedirect(r('acessos:grupos_permissoes', args=[obj.get_absolute_url().split('/')[2]]))


def perms_add(request,slug,id_perm):
	'''
		@perms_add: View para adicionar permissoes de um determinado user
	'''

	obj = User.objects.get(username=slug)	
	perm = Permission.objects.get(id=id_perm)
	obj.user_permissions.add(perm)
	return HttpResponseRedirect(r('acessos:grupos_permissoes', args=[obj.get_absolute_url().split('/')[2]]))

def perms_rem(request,slug,id_perm):
	'''
		@perms_rem: View para remover permissoes de um determinado user
	'''
	obj = User.objects.get(username=slug)
	perm = Permission.objects.get(id=id_perm)
	obj.user_permissions.remove(perm)
	return HttpResponseRedirect(r('acessos:grupos_permissoes', args=[obj.get_absolute_url().split('/')[2]]))

def grupo_detail(request,id):
	'''
		@grupo_detail: View para exibir os detalhes do grupo
	'''
	grupo = get_object_or_404(Group,id=id)
	return render(request,'acessos/grupo_detail.html',
		{'grupo':grupo}
		)

def grupo_create(request):
	'''
		@grupo_create: View para determinar se é um get ou post da url /grupo/
	'''
	if request.method == 'POST':
		return create_grupo(request)
	else:
		return new_grupo(request)

def new_grupo(request):
	'''
		@new_grupo: GET usado para renderizar o formulario na página
	'''
	return render(request, 'acessos/grupo_form.html',
		{'form': GrupoForm()})

def create_grupo(request):
	'''
		@create_grupo: POST Usado para recebimento de dados e criação do usuario caso tudo esteja correto
	'''
	form = GrupoForm(request.POST)
	if not form.is_valid():
		return render(request, 'acessos/grupo_form.html',
			{'form': form})
	obj = form.save()
	return HttpResponseRedirect('%d/' % obj.pk)


def grupo_suas_permissoes(request,grupo_id):
	'''
		@grupo_suas_permissoes:View que exibe todos os grupos que podem ser inseridos há um determinado grupo
	'''
	grupo = Group.objects.get(id=grupo_id)	
	#permissoes que o usuario possui
	permissoes_dentro = grupo.permissions.all()
	#permissoes que o usuario nao possui
	permissoes_fora = Permission.objects.exclude(name__startswith='can').exclude(id__in=grupo.permissions.all())	
	return render(request,'acessos/grupo_suas_permissions.html',
		{			
			'permissoes_fora':permissoes_fora,
			'permissoes_dentro':permissoes_dentro,
			'grupo':grupo
		}
		)

def grupos_permissoes_add(request,grupo_id,perm_id):
	'''
		@grupos_permissoes_add: View para adicionar permissoes de um determinado grupo
	'''

	grupo = Group.objects.get(id=grupo_id)	
	perm = Permission.objects.get(id=perm_id)
	grupo.permissions.add(perm)
	return HttpResponseRedirect(r('acessos:grupo_suas_permissoes', args=[grupo.id]))

def grupos_permissoes_rem(request,grupo_id,perm_id):
	'''
		@grupos_permissoes_rem: View para remover permissoes de um determinado grupo
	'''
	grupo = Group.objects.get(id=grupo_id)
	perm = Permission.objects.get(id=perm_id)
	grupo.permissions.remove(perm)
	return HttpResponseRedirect(r('acessos:grupo_suas_permissoes', args=[grupo.id]))

