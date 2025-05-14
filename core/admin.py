from django.contrib import admin
from .models import Cargo, Departamento, TipoContrato, Empleado, Rol, TipoPermiso, Permiso

# Register your models here.
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(TipoContrato)
admin.site.register(Empleado)
admin.site.register(Rol)
admin.site.register(TipoPermiso)
admin.site.register(Permiso)