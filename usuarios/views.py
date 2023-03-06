from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from main.models import *
from hashlib import sha256


def formatar_nome(nome):
    nome = nome.split(' ')
    for i in range(0, len(nome)):  # formatar o nome
        if len(nome[i]) >= 4:
            nome[i] = nome[i].capitalize()
        else:
            nome[i] = nome[i].lower()
    return ' '.join(nome)
    

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    if request.method == 'POST':
        nome = request.POST.get('nome').strip()
        nome = formatar_nome(nome)
        email = request.POST.get('email').strip()
        senha = request.POST.get('senha').strip()

        # testes de formulário
        if nome == '':
            return render(request, 'cadastro.html', {'status': 1,
                                                    'email': email,})
        
        if '@aluno.edu.es.gov.br' not in email:
            return render(request, 'cadastro.html', {'status': 2,
                                                    'nome': nome,})
        
        if len(Usuario.objects.filter(email=email)) > 0:  # usuário ja existe
            return render(request, 'cadastro.html', {'status': 3,
                                                    'nome': nome,})

        if len(senha) < 8:
            return render(request, 'cadastro.html', {'status': 4,
                                                    'nome': nome,
                                                    'email': email,})
        
        # formulario válido
        try:
            senha = sha256(senha.encode()).hexdigest()  # 'criptografa' a senha
            usuario = Usuario(nome=nome,
                            email=email,
                            senha=senha)
            usuario.save()
            
            perfil = Perfil(usuario=usuario)
            perfil.save()
            return redirect('auth/login/')
        
        except:  # erro interno do servidor
            return render(request, 'cadastro.html', {'status': 5,
                                                    'nome': nome,
                                                    'email': email,})





def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            senha = sha256(senha.encode()).hexdigest()  # 'criptografa' a senha
        
        except:  # erro interno do servidor
            return render(request, 'login.html', {'status': 1,
                                                 'email': email,})
        

        usuario = Usuario.objects.filter(email=email, senha=senha)
        if usuario.exists():
            request.session['usuario_tb'] = usuario[0].id
            return redirect('perfil')

        elif not usuario.exists():
            return render(request, 'login.html', {'status': 2,
                                                 'email': email,})
        
    
def sair(request):
    request.session['usuario_tb'] = None
    return redirect('login')

