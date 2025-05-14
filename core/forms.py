from .models import Cargo, Departamento, TipoContrato, Empleado, Rol
from django.forms import ModelForm, TextInput, DateInput, NumberInput
from django import forms
class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ['descripcion']

        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control'}),
        }

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion']

        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control'}),
        }

class ContratoForm(ModelForm):
    class Meta:
        model = TipoContrato
        fields = ['descripcion']

        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control'}),
        }

class EmpleadoForm(ModelForm):
    SEXO_CHOICES = [ 
        ('M', 'Masculino'), 
        ('F', 'Femenino'), 
    ]
    sexo = forms.ChoiceField(
        choices=SEXO_CHOICES   ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    TIPO_CONTRATO_CHOICES = TipoContrato.objects.all()
    tipo_contrato = forms.ModelChoiceField(
        queryset=TIPO_CONTRATO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    CARGO_CHOICES = Cargo.objects.all()
    cargo = forms.ModelChoiceField(
        queryset=CARGO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    DEPARTAMENTO_CHOICES = Departamento.objects.all()
    departamento = forms.ModelChoiceField(
        queryset=DEPARTAMENTO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Empleado
        fields = '__all__'

        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'cedula': TextInput(attrs={'class': 'form-control'}),
            'direccion': TextInput(attrs={'class': 'form-control'}),
            'sueldo': NumberInput(attrs={'class': 'form-control'}),
            'tipo_contrato': TextInput(attrs={'class': 'form-control'}),
        }

class RolForm(ModelForm):

    EMPLEADO_CHOICES = Empleado.objects.all()
    empleado = forms.ModelChoiceField(
        queryset=EMPLEADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Rol
        fields = '__all__'

        widgets = {
            'aniomes': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sueldo' : NumberInput(attrs={'class': 'form-control'}),
            'horas_extra' : NumberInput(attrs={'class': 'form-control'}),
            'bono' : NumberInput(attrs={'class': 'form-control'}),
            'iess' : NumberInput(attrs={'class': 'form-control'}),
            'tot_ing' : NumberInput(attrs={'class': 'form-control'}),
            'tot_des' : NumberInput(attrs={'class': 'form-control'}),
            'neto' : NumberInput(attrs={'class': 'form-control'})
        }
