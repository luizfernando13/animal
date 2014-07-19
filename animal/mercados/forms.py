# coding: utf-8

from django import forms
from animal.mercados.models import Anuncio



class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        