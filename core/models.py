from django.db import models

# Create your models here.
class Cargo(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion

class Departamento(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion

class TipoContrato(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ] 
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    tipo_contrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Rol(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    aniomes = models.DateField()#202501
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    horas_extra = models.DecimalField(max_digits=10, decimal_places=2)
    bono = models.DecimalField(max_digits=10, decimal_places=2)
    iess = models.DecimalField(max_digits=10, decimal_places=2)
    tot_ing = models.DecimalField(max_digits=10, decimal_places=2)
    tot_des = models.DecimalField(max_digits=10, decimal_places=2)
    neto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.empleado} - {self.empleado.cargo}"
    
class TipoPermiso(models.Model):

    descripcion = models.CharField(max_length=100)
    frecuencia_dias = models.BooleanField(default=True)
    def __str__(self):
        return self.descripcion

class Permiso(models.Model):

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_permiso = models.DateField()
    tipo_permiso = models.ForeignKey(TipoPermiso, on_delete=models.CASCADE)
    dias = models.PositiveIntegerField(null=True,blank=True)
    horas = models.PositiveIntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):

        return f"Permiso de {self.empleado.nombre} - {self.tipo_permiso.descripcion}"