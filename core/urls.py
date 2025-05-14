from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Cargo
    path('create_cargo', views.create_cargo, name="create_cargo"),
    path('update_cargo/<int:id>', views.update_cargo, name="update_cargo"),
    path('list_cargo', views.list_cargo, name="list_cargo"),
    path('delete_cargo/<int:id>', views.delete_cargo, name="delete_cargo"),
    # Departamento
    path('create_dep', views.create_dep, name="create_dep"),
    path('update_dep/<int:id>', views.update_dep, name="update_dep"),
    path('list_dep', views.list_dep, name="list_dep"),
    path('delete_dep/<int:id>', views.delete_dep, name="delete_dep"),
    # Tipo de contrato
    path('create_contrato', views.create_contrato, name="create_contrato"),
    path('update_contrato/<int:id>', views.update_contrato, name="update_contrato"),
    path('list_contrato', views.list_contrato, name="list_contrato"),
    path('delete_contrato/<int:id>', views.delete_contrato, name="delete_contrato"),
    # Empleado
    path('create_empleado', views.create_empleado, name="create_empleado"), 
    path('update_empleado/<int:id>', views.update_empleado, name="update_empleado"),
    path('list_empleado', views.list_empleado, name="list_empleado"),
    path('delete_empleado/<int:id>', views.delete_empleado, name="delete_empleado"),
    # Rol
    path('create_rol', views.create_rol, name="create_rol"),
    path('update_rol/<int:id>', views.update_rol, name="update_rol"),  
    path('list_rol', views.list_rol, name="list_rol"),
    path('delete_rol/<int:id>', views.delete_rol, name="delete_rol"),
]
