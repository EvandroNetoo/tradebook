from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import *
from django.db.models import Q


def formatar_nome(nome):
    nome = nome.split(' ')
    for i in range(0, len(nome)):  # formatar o nome
        if len(nome[i]) >= 4:
            nome[i] = nome[i].capitalize()
        else:
            nome[i] = nome[i].lower()
    return ' '.join(nome)
    

def catalogo(request):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
    # obrigatorio para o base

    categorias = Categorias.objects.all()[::-1]
    perfil = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    total = Livro.objects.filter(perfil = perfil).count()

    # da view

    livros = Livro.objects.filter(Q(vender=True) | Q(emprestar=True) | Q(trocar=True))
    livros = livros.exclude(perfil=perfil)
    
    return render(request, 'catalogo.html', {
        #obrigatorio
        'categorias': categorias,
        'total': total,
        'logado': True,
        #da view
        'livros': livros
    })


def buscar(request):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
    # obrigatorio para o base

    categorias = Categorias.objects.all()[::-1]
    perfil = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    total = Livro.objects.filter(perfil = perfil).count()

    # da view

    buscar_livro = request.POST.get('buscar_livro')

    livros = Livro.objects.filter(nome__icontains=buscar_livro)

    return render(request, 'buscar.html', {
        #obrigatorio
        'categorias': categorias,
        'total': total,
        'logado': True,
        #da view
        'livros': livros,
    })


def proposta(request, id_livro):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
    # obrigatorio para o base

    categorias = Categorias.objects.all()[::-1]
    perfil = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    total = Livro.objects.filter(perfil = perfil).count()

    # da view

    
    livro = Livro.objects.get(id=id_livro)

    if not livro.trocar and not livro.emprestar and not livro.trocar or livro.perfil == perfil:
        return redirect('seus_livros_todos')

    return render(request, 'proposta.html', {
        #obrigatorio
        'categorias': categorias,
        'total': total,
        'logado': True,
        #da view
        'livro': livro,
        'preco_venda': f'{livro.preco_venda:.2f}'.replace('.', ','),
        'preco_emprestimo': f'{livro.preco_emprestimo:.2f}'.replace('.', ','),
    })


def comprar_livro(request, id_livro):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    

    
   # da view


    return redirect('seus_livros_todos')

    
def pegar_emprestado_livro(request, id_livro):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
   # da view


    return redirect('seus_livros_todos')


def trocar_livro(request, id_livro):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
   # da view


    return redirect('seus_livros_todos')



def perfil(request):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
   # obrigatorio para o base

    categorias = Categorias.objects.all()[::-1]
    perfil_total = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    total = Livro.objects.filter(perfil = perfil_total).count()

    # da view

    usuario = Usuario.objects.get(id=request.session.get('usuario_tb'))
    
    return render(request, 'perfil.html', {
         #obrigatorio
        'categorias': categorias,
        'total': total,
        'logado': True,
        #da view
        'usuario': usuario,
    })


def seus_livros_todos(request):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
    # obrigatorio para o base

    categorias = Categorias.objects.all()[::-1]
    perfil_total = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    total = Livro.objects.filter(perfil = perfil_total).count()

    # da view
    perfil = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    livros = Livro.objects.filter(perfil = perfil)
    
    return render(request, 'seus_livros_todos.html', {
         #obrigatorio
        'categorias': categorias,
        'total': total,
        'logado': True,
        #da view
        'livros': livros
    })


def seus_livros_emprestados(request):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
    # obrigatorio para o base

    categorias = Categorias.objects.all()[::-1]
    perfil_total = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    total = Livro.objects.filter(perfil = perfil_total).count()

    # da view
    perfil = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    livros = Livro.objects.filter(perfil = perfil, emprestado=True)
    
    return render(request, 'seus_livros_emprestados.html', {
        #obrigatorio
        'categorias': categorias,
        'total': total,
        'logado': True,
        #da view
        'livros': livros
    })


def seus_livros_anunciados(request):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
    # obrigatorio para o base

    categorias = Categorias.objects.all()[::-1]
    perfil_total = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    total = Livro.objects.filter(perfil = perfil_total).count()

    # da view

    livros = Livro.objects.filter(Q(vender=True) | Q(emprestar=True) | Q(trocar=True), perfil=perfil_total)


    return render(request, 'seus_livros_anunciados.html', {
        #obrigatorio
        'categorias': categorias,
        'total': total,
        'logado': True,
        #view,
        'livros': livros,
        })


def detalhes_livro(request, id_livro):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
   # obrigatorio para o base

    categorias = Categorias.objects.all()[::-1]
    perfil = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    total = Livro.objects.filter(perfil = perfil).count()

    # da view

    livro = get_object_or_404(Livro, id=id_livro)

    if livro.perfil != perfil:
        return redirect('seus_livros_todos')


    return render(request, 'detalhes_livro.html', {
        #obrigatorio
        'categorias': categorias,
        'total': total,
        'logado': True,
        #da view
        'livro': livro,
        'preco_venda': f'{livro.preco_venda:.2f}',
        'preco_emprestimo': f'{livro.preco_emprestimo:.2f}',
    })


def adicionar_livro(request):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    
    if request.method == 'POST':
        
        # da view
        img = request.POST.get('img')
        nome = request.POST.get('nome')
        autor = request.POST.get('autor')
        autor = formatar_nome(autor)
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')

        vender = request.POST.get('vender')
        preco_venda = request.POST.get('preco_venda')

        emprestar = request.POST.get('emprestar')
        preco_emprestimo = request.POST.get('preco_emprestimo')

        trocar = request.POST.get('trocar')

        if int(categoria) == 0:
            return redirect('perfil')

        perfil = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
        livro = Livro(
            img = img,
            nome = nome,
            autor = autor,
            descricao = descricao,
            categoria = Categorias.objects.get(id=categoria),
            perfil = perfil,
            trocar = True if trocar == 'on' else False
        )

        if vender:
            print(type(vender))
            livro.vender = True
            livro.preco_venda = preco_venda
        else:
            print('oi2')
            livro.vender = False

        if emprestar:
            print('oi3')
            livro.emprestar = True
            livro.preco_emprestimo = preco_emprestimo
        else:
            print('oi4')
            livro.emprestar = False

        livro.save()

        return redirect('perfil')


def atualizar_livro(request, id_livro):
    if not request.session.get('usuario_tb'):
        return redirect('login')
    

    livro = get_object_or_404(Livro, id=id_livro)

    perfil = Perfil.objects.get(usuario_id = request.session.get('usuario_tb'))
    if livro.perfil != perfil:
        return redirect('seus_livros_todos')
    
    nome = request.POST.get('nome')
    autor = request.POST.get('autor')
    autor = formatar_nome(autor)
    descricao = request.POST.get('descricao')
    categoria = request.POST.get('categoria')

    vender = request.POST.get('vender')
    preco_venda = request.POST.get('preco_venda')

    emprestar = request.POST.get('emprestar')
    preco_emprestimo = request.POST.get('preco_emprestimo')

    trocar = request.POST.get('trocar')


    livro.nome = nome
    livro.autor = autor
    livro.descricao = descricao
    categoria = Categorias.objects.get(id=categoria)
    livro.categoria = categoria

    livro.trocar = True if trocar else False

    livro.vender = True if vender else False
    livro.preco_venda = preco_venda if vender else 0

    livro.emprestar = True if emprestar else False
    livro.preco_emprestimo = preco_emprestimo if emprestar else 0

    livro.save()

    return redirect('seus_livros_todos')


def excluir_livro(request, id_livro):

    return redirect('seus_livros_todos')