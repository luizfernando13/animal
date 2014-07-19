# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

SEXO = (
        ('M', 'Macho'),
        ('F', 'Fêmea'),
        )
class Raca(models.Model):
    raca = models.CharField(max_length=80,verbose_name='Espécie')
    def __str__(self):
        return self.raca

class TipoAnimal(models.Model):
    especie = models.CharField(max_length=80,verbose_name='Espécie')
    def __str__(self):
        return self.especie

class Animal(models.Model):
    name = models.CharField(max_length=80,verbose_name='Descrição',blank=True)
    especie = models.ForeignKey(TipoAnimal,verbose_name='Espécie',related_name='animais',blank=True,null=True)
    raca = models.ForeignKey(Raca,verbose_name='Raça',related_name='animais',blank=True,null=True)
    sexo = models.CharField(max_length=1,choices=SEXO,default='M')
    created_at = models.DateTimeField(auto_now_add = True)
    #user = models.ForeignKey(User,related_name='animais')

    def __str__(self):
        return self.name

    @models.permalink
    def detail(self):
        return ('animais:animal_detail', (), {'id': self.id})

    @models.permalink
    def edit(self):
        return ('animais:animal_edit', (), {'id': self.id})