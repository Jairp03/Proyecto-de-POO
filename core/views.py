from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

# Create your views here.
def home (request):
    return render(request, 'home.html')

def signup (request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registrar usuario
            try:
                user = User.objects.create_user(username = request.POST['username'], password= request.POST['password2'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                'form': UserCreationForm(),
                "error": 'El usuario ya existe',
                })
        return render(request, 'signup.html', {
        'form': UserCreationForm(),
        "error": 'Las contraseñas no coinciden',
        })
def signin (request):
    if request.method == 'GET':
        return render (request, 'signin.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render (request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')

def logoutuser(request):
    logout(request)
    return redirect('home')

def create (request):
    pass

def update (request):
    pass

def list (request):
    pass

def delete (request):
    pass