from rest_framework import serializers
from .models import *

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

class PersonaXCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaXCargo
        fields = '__all__'

class VehiculoVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoVenta
        fields = '__all__'

class VehiculoReparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoReparacion
        fields = '__all__'

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class InventarioPorSucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioPorSucursal
        fields = '__all__'

class CotizacionReparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotizacionReparacion
        fields = '__all__'

class RepuestoVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepuestoVenta
        fields = '__all__'

class CotizacionRepuestosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotizacionRepuestos
        fields = '__all__'

class CotizacionVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotizacionVehiculo
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class CategoriaInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaInventario
        fields = '__all__'
