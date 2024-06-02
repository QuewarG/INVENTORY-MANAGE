from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db import IntegrityError
from django.utils.translation import gettext as _, activate
from django.conf import settings
from .forms import *

# Importaciones restframework
from rest_framework import viewsets
from .serializer import *
from .models import *


# CREACIÓN DE LAS VISTAS PARA EL ACCESO A LA API
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class PersonaXCargoViewSet(viewsets.ModelViewSet):
    queryset = PersonaXCargo.objects.all()
    serializer_class = PersonaXCargoSerializer

class VehiculoVentaViewSet(viewsets.ModelViewSet):
    queryset = VehiculoVenta.objects.all()
    serializer_class = VehiculoVentaSerializer

class VehiculoReparacionViewSet(viewsets.ModelViewSet):
    queryset = VehiculoReparacion.objects.all()
    serializer_class = VehiculoReparacionSerializer

class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class InventarioPorSucursalViewSet(viewsets.ModelViewSet):
    queryset = InventarioPorSucursal.objects.all()
    serializer_class = InventarioPorSucursalSerializer

class CotizacionReparacionViewSet(viewsets.ModelViewSet):
    queryset = CotizacionReparacion.objects.all()
    serializer_class = CotizacionReparacionSerializer

class RepuestoVentaViewSet(viewsets.ModelViewSet):
    queryset = RepuestoVenta.objects.all()
    serializer_class = RepuestoVentaSerializer

class CotizacionRepuestosViewSet(viewsets.ModelViewSet):
    queryset = CotizacionRepuestos.objects.all()
    serializer_class = CotizacionRepuestosSerializer

class CotizacionVehiculoViewSet(viewsets.ModelViewSet):
    queryset = CotizacionVehiculo.objects.all()
    serializer_class = CotizacionVehiculoSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class CategoriaInventarioViewSet(viewsets.ModelViewSet):
    queryset = CategoriaInventario.objects.all()
    serializer_class = CategoriaInventarioSerializer
