from django.urls import path, include
from .views import *

# REST FRAMEWORK
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

# Creacion del router encargado de la gestion de rutas en la API
router = routers.DefaultRouter()

# Generacion de rutas por medio de Rest Framework
router.register(r'Rol', RolViewSet, basename='Rol')
router.register(r'Usuario', UsuarioViewSet, basename='Usuario')
router.register(r'Cargo', CargoViewSet, basename='Cargo')
router.register(r'PersonaXCargo', PersonaXCargoViewSet, basename='PersonaXCargo')
router.register(r'VehiculoVenta', VehiculoVentaViewSet, basename='VehiculoVenta')
router.register(r'VehiculoReparacion', VehiculoReparacionViewSet, basename='VehiculoReparacion')
router.register(r'OrdenTrabajo', OrdenTrabajoViewSet, basename='OrdenTrabajo')
router.register(r'Inventario', InventarioViewSet, basename='Inventario')
router.register(r'CotizacionReparacion', CotizacionReparacionViewSet, basename='CotizacionReparacion')
router.register(r'RepuestoVenta', RepuestoVentaViewSet, basename='RepuestoVenta')
router.register(r'CotizacionRepuestos', CotizacionRepuestosViewSet, basename='CotizacionRepuestos')
router.register(r'CotizacionVehiculo', CotizacionVehiculoViewSet, basename='CotizacionVehiculo')
router.register(r'Factura', FacturaViewSet, basename='Factura')
router.register(r'CategoriaInventario', CategoriaInventarioViewSet, basename='CategoriaInventario')


urlpatterns = [
    # ENRUTAMIENTO API
    path("api/", include(router.urls) ),
    # Documentacion Api
    path('docs/', include_docs_urls(title="How to Use API")),

]
