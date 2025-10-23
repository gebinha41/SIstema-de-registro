from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Funcionario
import base64
import cv2
import numpy as np
from django.db import models

def login_view(request):
    """Página de login com usuário/senha e reconhecimento facial."""
    if request.method == 'POST':
        # Lógica de login com usuário e senha
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'registro/login.html', {'error': 'Usuário ou senha inválidos'})
    return render(request, 'registro/login.html')

@login_required
def dashboard(request):
    """Dashboard do usuário após o login."""
    try:
        funcionario = request.user.funcionario
    except Funcionario.DoesNotExist:
        funcionario = None
    return render(request, 'registro/dashboard.html', {'funcionario': funcionario})

@login_required
def logout_view(request):
    """Faz o logout do usuário."""
    logout(request)
    return redirect('login')

def reconhecer_rosto(request):
    """Endpoint para reconhecimento facial (placeholder)."""
    if request.method == 'POST':
        # A lógica completa de reconhecimento facial seria implementada aqui.
        return JsonResponse({'success': True, 'message': 'Reconhecimento facial simulado com sucesso!'})
    return JsonResponse({'success': False, 'message': 'Método inválido'})

# registro/views.py
from django.shortcuts import render, redirect

def cadastro_view(request):
    if request.method == 'POST':
        # lógica de cadastro aqui
        pass
    return render(request, 'registro/cadastro.html')
