# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User


class Anuncio(models.Model):
    '''
        @Ano: Modelo de dados da tabela Ano (Serie)
    '''    
    name = models.CharField(max_length=80,verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add = True)
    animal = models.ForeignKey('animais.Animal',verbose_name='Animalandro')
    #user = models.ForeignKey(User,related_name='anuncios')

    @models.permalink
    def detail(self):
        return ('mercados:anuncio_detail', (), {'id': self.id})

    @models.permalink
    def edit(self):
        return ('mercados:anuncio_edit', (), {'id': self.id})

    def __str__(self):
        return self.name
