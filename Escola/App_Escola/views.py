from django.shortcuts import render
from .models import Professor, Turma, Atividade
from django.db import connection, transaction
from django.contrib import messages
from hashlib import sha256
from django.http import HttpResponse

def abre_index(request):
    dado_pesquisa = 'Obama'
    verifica_populado = Professor.objects.filter(nome__icontains=dado_pesquisa)

    if len(verifica_populado) == 0:
        print('Não está populado')
        initial_population()
    else:
        ('Achei Obama', verifica_populado)

    return render(request, 'login.html')

def enviar_login(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha_criptografada = sha256(senha.encode()).hexdigest()
        dados_professor = Professor.objects.filter(email=email).values('nome', 'senha', 'id')
        print('Dados do Professor', dados_professor)

        if dados_professor:
            senha = dados_professor[0]
            senha = senha['senha']
            usuario_logado = dados_professor[0]
            usuario_logado = usuario_logado['nome']
            if (senha == senha_criptografada):
                messages.info(request, 'Bem vindo.')

                mensagem = "Olá professor, " + email + "Seja bem vindo!!"
                return HttpResponse(mensagem) 
            else: 
                messages.info(request, 'Usuário ou senha incorretos. Tente Novamente.')
                return render(request, 'login.html')
            
    messages.info(request, "Olá" + email + ", seja bem-vindo! Percebemos que você é novo por aqui. Complete o seu cadastro.")
    return render(request,'cadastro.html', {'login': email})

def confirmar_cadastro(request):
     if (request.method == 'POST'):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha_criptografada = sha256(senha.encode()).hexdigest()

        grava_professor = Professor(
            nome = nome,
            email = email,
            senha=senha_criptografada
        )
        grava_professor.save()

        mensagem = "Olá Professor " + nome + ", Seja bem-vindo!"
        return HttpResponse(mensagem)


def initial_population():
    print('Vou popular')
    cursor = connection.cursor()

    senha = "123456"
    senha_armazenar = sha256(senha.encode()).hexdigest()

    insert_sql_professor = "INSERT INTO App_Escola_professor (nome, email, senha) VALUES"
    insert_sql_professor = insert_sql_professor + "('Prof. Barak Obama', 'barak.obama@gmail.com', '"+ senha_armazenar + "'),"
    insert_sql_professor = insert_sql_professor + "('Profa. Angela Merkel', 'angela.merkel@gmail.com', '"+ senha_armazenar + "'),"
    insert_sql_professor = insert_sql_professor + "('Prof. Xi Jinping', 'xi.jinping@gmail.com', '"+ senha_armazenar + "'),"

    cursor.execute(insert_sql_professor)
    transaction.atomic()

    insert_sql_turma = "INSERT INTO App_Escola_turma (nome_turma, id_professor_id) VALUES"
    insert_sql_turma = insert_sql_turma + "('1o Semestre - Desenvolvimento de Sistemas',1),"
    insert_sql_turma = insert_sql_turma + "('2o Semestre - Desenvolvimento de Sistemas',2),"
    insert_sql_turma = insert_sql_turma + "('3o Semestre - Desenvolvimento de Sistemas',3),"

    cursor.execute(insert_sql_turma)
    transaction.atomic()

    insert_sql_atividade = "INSERT INTO App_Escola_atividade (nome_atividade, id_turma_id) VALUES"
    insert_sql_atividade = insert_sql_atividade + "('Apresentar Fundamentos da Programação', 1),"
    insert_sql_atividade = insert_sql_atividade + "('Apresentar Framework Django', 2),"
    insert_sql_atividade = insert_sql_atividade + "('Apresentar conceitos de Gerenciamento de Projetos', 3)"

    cursor.execute(insert_sql_atividade)
    transaction.atomic()

    print('Populei')
    

    
