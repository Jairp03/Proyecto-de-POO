from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from core.forms import CargoForm, DepartamentoForm, ContratoForm, EmpleadoForm, RolForm
from .models import Cargo, Departamento, TipoContrato, Empleado, Rol

# Create your views here.
#*****Autenticacion*****
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

@login_required
def logoutuser(request):
    logout(request)
    return redirect('home')

#*****CRUD Cargos*****
@login_required
def create_cargo (request):
    context={'title':'Ingresar cargo'}
    print("metodo: ",request.method)
    if request.method == "GET":
        
        form = CargoForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'cargos/create.html', context)
    else:
        #  print("entro por post")
        form = CargoForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            return redirect('core:list_cargo')
        else:
            context['form'] = form
            return render(request, 'cargos/create.html', context) 

@login_required
def update_cargo (request, id):
   context={'title':'Actualizar Cargo'}
   cargo = Cargo.objects.get(pk=id)
   if request.method == "GET":
      form = CargoForm(instance=cargo)
      context['form'] = form
      return render(request, 'cargos/create.html', context)
   else:
      form = CargoForm(request.POST,instance=cargo)
      if form.is_valid():
          form.save()
          return redirect('core:list_cargo')
      else:
          context['form'] = form
          return render(request, 'cargos/create.html', context)

@login_required
def list_cargo (request):
    query= request.GET.get('q',None)
    print(query)
    if query: cargos = Cargo.objects.filter(descripcion__icontains=query)
    else: cargos = Cargo.objects.all()
    context = {'cargos': cargos, 'title': 'Listado de nomina'} 
    return render(request, 'cargos/list.html', context)

@login_required
def delete_cargo (request, id):
    cargo=None
    try:
        cargo = Cargo.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Cargo a Eliminar','cargo':cargo,'error':''}
            return render(request, 'cargos/delete.html',context)  
        else: 
            cargo.delete()
            return redirect('core:list_cargo')
    except:
        context = {'title':'Eliminar','cargo':cargo,'error':'Error al eliminar'}
        return render(request, 'cargos/delete.html', context)
    
#*****CRUD Departamentos*****
@login_required
def create_dep (request):
    context={'title':'Ingresar departamento'}
    print("metodo: ",request.method)
    if request.method == "GET":
        
        form = DepartamentoForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'departamentos/create.html', context)
    else:
        #  print("entro por post")
        form = DepartamentoForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            return redirect('core:list_dep')
        else:
            context['form'] = form
            return render(request, 'departamentos/create.html', context) 

@login_required
def update_dep (request, id):
   context={'title':'Actualizar Departamento'}
   deps = Departamento.objects.get(pk=id)
   if request.method == "GET":
      form = DepartamentoForm(instance=deps)
      context['form'] = form
      return render(request, 'departamentos/create.html', context)
   else:
      form = DepartamentoForm(request.POST,instance=deps)
      if form.is_valid():
          form.save()
          return redirect('core:list_dep')
      else:
          context['form'] = form
          return render(request, 'departamentos/create.html', context)

@login_required
def list_dep (request):
    query= request.GET.get('q',None)
    print(query)
    if query: deps = Departamento.objects.filter(descripcion__icontains=query)
    else: deps = Departamento.objects.all()
    context = {'deps': deps, 'title': 'Listado de departamentos'} 
    return render(request, 'departamentos/list.html', context)

@login_required
def delete_dep (request, id):
    deps=None
    try:
        deps = Departamento.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Departamento a Eliminar', 'deps':deps,'error':''}
            return render(request, 'departamentos/delete.html',context)  
        else: 
            deps.delete()
            return redirect('core:list_dep')
    except:
        context = {'title':'Eliminar','cargo':deps,'error':'Error al eliminar'}
        return render(request, 'departamentos/delete.html', context)
    
#*****CRUD Tipo de contrato*****
@login_required
def create_contrato (request):
    context={'title':'Ingresar tipo de contrato'}
    print("metodo: ",request.method)
    if request.method == "GET":
        
        form = ContratoForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'contratos/create.html', context)
    else:
        #  print("entro por post")
        form = ContratoForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            return redirect('core:list_contrato')
        else:
            context['form'] = form
            return render(request, 'contratos/create.html', context) 

@login_required
def update_contrato (request, id):
   context={'title':'Actualizar Contrato'}
   contrato = TipoContrato.objects.get(pk=id)
   if request.method == "GET":
      form = ContratoForm(instance=contrato)
      context['form'] = form
      return render(request, 'contratos/create.html', context)
   else:
      form = ContratoForm(request.POST,instance=contrato)
      if form.is_valid():
          form.save()
          return redirect('core:list_contrato')
      else:
          context['form'] = form
          return render(request, 'contratos/create.html', context)

@login_required
def list_contrato (request):
    query= request.GET.get('q',None)
    print(query)
    if query: contratos = TipoContrato.objects.filter(descripcion__icontains=query)
    else: contratos = TipoContrato.objects.all()
    context = {'contratos': contratos, 'title': 'Listado de nomina'} 
    return render(request, 'contratos/list.html', context)

@login_required
def delete_contrato (request, id):
    contrato=None
    try:
        contrato = TipoContrato.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'contrato a Eliminar','contrato':contrato,'error':''}
            return render(request, 'contratos/delete.html',context)  
        else: 
            contrato.delete()
            return redirect('core:list_contrato')
    except:
        context = {'title':'Eliminar','contrato':contrato,'error':'Error al eliminar'}
        return render(request, 'contratos/delete.html', context)

#*****CRUD Empleados*****
@login_required
def create_empleado (request):
    context={'title':'Ingresar el nombre del empleado'}
    print("metodo: ",request.method)
    if request.method == "GET":
        
        form = EmpleadoForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'empleados/create.html', context)
    else:
        #  print("entro por post")
        form = EmpleadoForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            return redirect('core:list_empleado')
        else:
            context['form'] = form
            return render(request, 'empleados/create.html', context) 

@login_required
def update_empleado (request, id):
   context={'title':'Actualizar Empleado'}
   empleado = Empleado.objects.get(pk=id)
   if request.method == "GET":
      form = EmpleadoForm(instance=empleado)
      context['form'] = form
      return render(request, 'empleados/create.html', context)
   else:
      form = EmpleadoForm(request.POST,instance=empleado)
      if form.is_valid():
          form.save()
          return redirect('core:list_empleado')
      else:
          context['form'] = form
          return render(request, 'empleados/create.html', context)

@login_required
def list_empleado (request):
    query= request.GET.get('q',None)
    print(query)
    if query: empleados = Empleado.objects.filter(nombre__icontains=query)
    else: empleados = Empleado.objects.all()
    context = {'empleados': empleados, 'title': 'Listado de nomina'} 
    return render(request, 'empleados/list.html', context)

@login_required
def delete_empleado (request, id):
    empleado=None
    try:
        empleado = Empleado.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Empleado a Eliminar','empleado':empleado,'error':''}
            return render(request, 'empleados/delete.html',context)  
        else: 
            empleado.delete()
            return redirect('core:list_empleado')
    except:
        context = {'title':'Eliminar','empleado':empleado,'error':'Error al eliminar'}
        return render(request, 'empleado/delete.html', context)
    
#*****CRUD Rol*****
@login_required
def create_rol (request):
    context={'title':'Ingresar el nombre el Rol'}
    print("metodo: ",request.method)
    if request.method == "GET":
        
        form = RolForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'Roles/create.html', context)
    else:
        #  print("entro por post")
        form = RolForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            return redirect('core:list_rol')
        else:
            context['form'] = form
            return render(request, 'roles/create.html', context) 

@login_required
def update_rol (request, id):
   context={'title':'Actualizar Rol'}
   rol = Rol.objects.get(pk=id)
   if request.method == "GET":
      form = RolForm(instance=rol)
      context['form'] = form
      return render(request, 'roles/create.html', context)
   else:
      form = RolForm(request.POST,instance=rol)
      if form.is_valid():
          form.save()
          return redirect('core:list_rol')
      else:
          context['form'] = form
          return render(request, 'roles/create.html', context)

@login_required
def list_rol (request):
    query = request.GET.get('q',None)
    print(query)
    if query: roles = Rol.objects.filter(empleado__nombre__icontains=query)
    else: roles = Rol.objects.all()
    context = {'roles': roles, 'title': 'Listado de nomina'} 
    return render(request, 'roles/list.html', context)

@login_required
def delete_rol (request, id):
    rol=None
    try:
        rol = Rol.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Rol a Eliminar','rol':rol,'error':''}
            return render(request, 'roles/delete.html',context)  
        else: 
            rol.delete()
            return redirect('core:list_rol')
    except:
        context = {'title':'Eliminar','rol':rol,'error':'Error al eliminar'}
        return render(request, 'rol/delete.html', context)