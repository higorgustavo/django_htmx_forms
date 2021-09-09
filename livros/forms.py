from django import forms
from django.db.models import fields
from django.forms.models import inlineformset_factory, modelform_factory, modelformset_factory
from .models import Autor, Livro


class AutorForm(forms.ModelForm):
    class Meta:
        models = Autor
        fields = ['nome']


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'numero_paginas']

