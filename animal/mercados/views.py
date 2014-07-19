# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from animal.mercados.forms import AnuncioForm
from animal.mercados.models import Anuncio
#comment
import random

def anuncios(request):
    anuncios = Anuncio.objects.all().order_by('-created_at')
    return render(request,'mercados/compra_venda.html',{'anuncios':anuncios})   


def anuncio_edit(request,id): 
    '''
        @anuncio_edit: View para determinar se é um GET ou POST para editar um anuncio
    '''
    anuncio = get_object_or_404(Anuncio,id=id)
    if request.method == 'POST':
        return edit_anuncio(request,anuncio)
    else:
        return request_anuncio(request,anuncio)

#not tested ( be careful if need refactor)
def edit_anuncio(request,anuncio):
    '''
        @edit_anuncio: View para alterar os dados de um anuncio
    '''    
    form = AnuncioForm(request.POST,instance=anuncio)
    if form.is_valid():
        anuncio = form.save(commit=False)
        anuncio.save()
        return HttpResponseRedirect(anuncio.detail())
    else:
        return render(request,'mercados/anuncio_edit.html',{'form':form})

def request_anuncio(request,anuncio):
    '''
        @request_anuncio: View para obter os dados de um determinado anuncio
    '''    
    form = AnuncioForm(instance=anuncio)
    return render(request, 'mercados/anuncio_edit.html', {'form': form,'anuncio':anuncio})

def anuncio_detail(request,id):
    
    anuncio = get_object_or_404(Anuncio,id=id)
    anuncios = Anuncio.objects.filter(animal__raca__raca=anuncio.animal.raca.raca).exclude(id=anuncio.id).order_by('-created_at')
    anuncios = anuncios[:30]
    anuncios = sorted(anuncios, key=lambda x: random.random())
    return render(request,'mercados/anuncio_detail.html',
        {'anuncio':anuncio,'anuncios':anuncios[:4]}
        )

def anuncio_create(request):
    if request.method == 'POST':        
        return create_anuncio(request)
    else:
        return new_anuncio(request)

def new_anuncio(request):
    return render(request, 'mercados/anuncio_form.html',
        {'form': AnuncioForm()})

def create_anuncio(request):
    form = AnuncioForm(request.POST)
    if not form.is_valid():
        return render(request, 'mercados/anuncio_form.html',
            {'form': form})
    obj = form.save()
    obj.save()
    return HttpResponseRedirect(obj.detail())
