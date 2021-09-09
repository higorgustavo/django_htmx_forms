from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Autor, Livro
from .forms import LivroForm, AutorForm


def list_autores(request):
    autores = Autor.objects.all()
    context = {
        "autores": autores
    }
    return render(request, "autores/list_autores.html", context)


# Livros


def list_livros(request):
    livros = Livro.objects.select_related("autor").all()
    context = {
        "livros": livros
    }
    return render(request, "livros/list_livros.html", context)


def create_livro(request, id):
    autor = Autor.objects.get(pk=id)
    livros = Livro.objects.select_related("autor").filter(autor=autor)
    form = LivroForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            livro = form.save(commit=False)
            livro.autor = autor
            livro.save()
            return redirect('detail-livro', id=livro.id)
        else:
            context = {
                "form": form,
            }
            return render(request, "livros/livro_form.html", context) 

    context = {
        "form": form,
        "autor": autor,
        "livros": livros
    }
    return render(request, "livros/create_livro.html", context)


def detail_livro(request, id):
    livro = Livro.objects.get(pk=id)
    context = {
        "livro": livro
    }
    return render(request, "livros/detail_livro.html", context)


def update_livro(request, id):
    livro = Livro.objects.get(pk=id)
    form = LivroForm(request.POST or None, instance=livro)

    if request.method == "POST":
        if form.is_valid():
            livro = form.save()
            return redirect('detail-livro', id=livro.id)

    context = {
        "livro": livro,
        "form": form
    }
    return render(request, "livros/livro_form.html", context) 


def delete_livro(request, id):
    livro = Livro.objects.get(pk=id)
    livro.delete()
    return HttpResponse('')  


def create_livro_form(request):
    form = LivroForm()
    context = {
        "form": form
    }
    return render(request, "livros/livro_form.html", context)