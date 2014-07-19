# coding: utf-8

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.db import IntegrityError
from django.contrib.auth.models import Group



class GrupoForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name',)


    def clean_name(self):
    	'''
    		@clean_name: Transforma o nome do grupo em capitalizado
    	'''
        name = self.cleaned_data['name']
        words = map(lambda w: w.capitalize(), name.split())
        capitalized_name = ' '.join(words)
        return capitalized_name




