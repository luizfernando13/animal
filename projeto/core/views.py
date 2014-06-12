#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import Group,User
"""
#@login required
def pessoas(request):
	return render(request,'pessoas.html')

def index(request):
	return render(request,'index.html')

def home(request):
	return render(request,'index.html')

def homepage2(request):
	return render(request,'index.html')
"""
"""
from projeto.dia.models import Dia
from projeto.disciplina.models import Disciplina
from projeto.horario.models import Horario
from projeto.turma.models import Turma
from projeto.aula.models import Aula
def config(request):
	seg = Dia.objects.create(nome='Segunda')
	ter = Dia.objects.create(nome='Terca')
	Dia.objects.create(nome='Quarta')
	qui = Dia.objects.create(nome='Quinta')
	sex =  Dia.objects.create(nome='Sexta')
	sab = Dia.objects.create(nome='Sabado')
	hor7 =  Horario.objects.create(inicio='7:00',fim='8:00')
	hor8 =  Horario.objects.create(inicio='8:00',fim='9:00')
	hor9 =  Horario.objects.create(inicio='9:00',fim='10:00')
	hor10 = Horario.objects.create(inicio='10:00',fim='11:00')
	hor11 = Horario.objects.create(inicio='11:00',fim='12:00')
	tur = Turma.objects.create(nome='Turma 001',turno = 'M',ano_letivo='2014',sala='001',max_aluno=50,total_aluno=10)
	
	
	di1= Disciplina.objects.create(nome='Matematica')
	di2 =Disciplina.objects.create(nome='Biologia')
	di3=Disciplina.objects.create(nome='Fisica')
	di4=Disciplina.objects.create(nome='Ciencia')

	Aula.objects.create(horario=hor7,turma=tur,disciplina=di1,dia=seg)
	Aula.objects.create(horario=hor8,turma=tur,disciplina=di1,dia=seg)
	Aula.objects.create(horario=hor9,turma=tur,disciplina=di2,dia=seg)
	Aula.objects.create(horario=hor10,turma=tur,disciplina=di2,dia=seg)

	Aula.objects.create(horario=hor7,turma=tur,disciplina=di4,dia=ter)
	Aula.objects.create(horario=hor10,turma=tur,disciplina=di4,dia=ter)
	Aula.objects.create(horario=hor11,turma=tur,disciplina=di2,dia=ter)

	Aula.objects.create(horario=hor7,turma=tur,disciplina=di4,dia=qui)
	Aula.objects.create(horario=hor10,turma=tur,disciplina=di4,dia=qui)
	Aula.objects.create(horario=hor11,turma=tur,disciplina=di4,dia=qui)

	Group.objects.create(name='ADMINISTRADOR GERAL')
	Group.objects.create(name='DIRETOR RH')
	Group.objects.create(name='GERENTE RH')
	Group.objects.create(name='OPERADOR RH')
	Group.objects.create(name='DIRETOR ACADEMICO')
	Group.objects.create(name='GERENTE ACADEMICO')
	Group.objects.create(name='OPERADOR ACADEMICO')
	Group.objects.create(name='DIRETOR ESTATISTICO')
	Group.objects.create(name='GERENTE ESTATISTICO')
	Group.objects.create(name='OPERADOR ESTATISTICO')
	Group.objects.create(name='DIRETOR ESCOLAR')
	Group.objects.create(name='GERENTE ESCOLAR')
	Group.objects.create(name='OPERADOR ESCOLAR')
	Group.objects.create(name='PROFESSOR')
	Group.objects.create(name='ALUNO')
	Group.objects.create(name='RESPONSAVEL')

	return render(request,'index.html')

	"""