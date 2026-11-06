from django.shortcuts import render, redirect
from .models import Filme

def inicio(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        diretor = request.POST.get('diretor')
        ano = request.POST.get('ano')

        Filme.objects.create(
            titulo=titulo,
            diretor=diretor,
            ano=ano
        )
        return redirect('/')

    filmes = Filme.objects.all()
    return render(request, 'inicio.html', {'filmes': filmes})


def editar_filme(request, id):
    filme = Filme.objects.get(id=id)

    if request.method == 'POST':
        filme.titulo = request.POST.get('titulo')
        filme.diretor = request.POST.get('diretor')
        filme.ano = request.POST.get('ano')
        filme.save()
        return redirect('/')

    return render(request, 'editar.html', {'filme': filme})


def excluir_filme(request, id):
    if request.method == 'POST':
        filme = Filme.objects.get(id=id)
        filme.delete()

    return redirect('/')
