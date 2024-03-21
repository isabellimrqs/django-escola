from django.shortcuts import render
from .models import Professor, Turma, Atividade
from django.db import connection, transaction
from django.contrib import messages
from hashlib import sha256

def abre_index(request):
    return render(request, 'login.html')

def enviar_login(request):
    return render(request,'dados_ok.html')

def initial_population():
    print('Vou popular')
    cursor = connection.cursor()

    senha = "123456"
    senha_armazenar = sha256(senha.encode()).hexdigest()

    insert_sql_professor = "INSERT INTO App_SimSAEP_professor (nome, email, senha) VALUES"
    insert_sql_professor = insert_sql_professor + "('Prof. Barak Obama', 'barak.obama@gmail.com', '"+ senha_armazenar + "'),"
    insert_sql_professor = insert_sql_professor + "('Profa. Angela Merkel', 'angela.merkel@gmail.com', '"+ senha_armazenar + "'),"
    insert_sql_professor = insert_sql_professor + "('Prof. Xi Jinping', 'xi.jinping@gmail.com', '"+ senha_armazenar + "'),"

    cursor.execute(insert_sql_professor)
    transaction.atomic()

    insert_sql_turma = "INSERT INTO App_SimSAEP_turma (nome_turma, id_professor_id) VALUES"
    insert_sql_turma = insert_sql_turma + "('1o Semestre - Desenvolvimento de Sistemas',1),"
    insert_sql_turma = insert_sql_turma + "('2o Semestre - Desenvolvimento de Sistemas',2),"
    insert_sql_turma = insert_sql_turma + "('3o Semestre - Desenvolvimento de Sistemas',3),"

    cursor.execute(insert_sql_turma)
    transaction.atomic()

    
