from django.db import models


class Autor(models.Model):
    nome = models.CharField("Autor", max_length=100)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField("Título", max_length=250) 
    numero_paginas = models.PositiveIntegerField(default=1)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo