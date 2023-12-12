from django.shortcuts import render
from django.http import HttpResponse

nome = 'Paulo'

# Create your views here.
def ver_produto(request):
    return render(request, 'ver_produto.html', {'nome': f'{nome}'})


def inserir_produto(request):
    return HttpResponse('inserir produto')