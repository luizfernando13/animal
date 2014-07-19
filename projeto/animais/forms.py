# coding: utf-8

from django import forms
from projeto.animais.models import Animal



class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        