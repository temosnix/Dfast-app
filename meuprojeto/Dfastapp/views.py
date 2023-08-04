from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import login_form
from .models import senhas

# Create your views here.

def home (request):
    data ={}
    form = login_form()
    data['form'] = form

    return render(request,'dfastapp/home.html', data)


def processar_login (request):
    form = login_form(request.POST)
    nome = form.data['usuario']
    senha = form.data['senha']
    db_data = senhas.objects.get(id=1)
    db_nome = db_data.nome
    db_senha = db_data.senha
    if nome == db_nome and senha == db_senha:
        return render(request,'dfastapp/opcao.html')
    else:
        return HttpResponse('Senha ou usuario incorreto')
