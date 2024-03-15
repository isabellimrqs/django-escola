from django.shortcuts import render

def abre_index(request):
    return render(request, 'login.html')

def enviar_login(request):
    return render(request,'dados_ok.html')

