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
router.register(r'Sucursal', SucursalViewSet, basename='Sucursal')
router.register(r'PersonaXCargo', PersonaXCargoViewSet, basename='PersonaXCargo')
router.register(r'VehiculoVenta', VehiculoVentaViewSet, basename='VehiculoVenta')
router.register(r'VehiculoReparacion', VehiculoReparacionViewSet, basename='VehiculoReparacion')
router.register(r'OrdenTrabajo', OrdenTrabajoViewSet, basename='OrdenTrabajo')
router.register(r'Inventario', InventarioViewSet, basename='Inventario')
router.register(r'InventarioPorSucursal', InventarioPorSucursalViewSet, basename='InventarioPorSucursal')
router.register(r'CotizacionReparacion', CotizacionReparacionViewSet, basename='CotizacionReparacion')
router.register(r'RepuestoVenta', RepuestoVentaViewSet, basename='RepuestoVenta')
router.register(r'CotizacionRepuestos', CotizacionRepuestosViewSet, basename='CotizacionRepuestos')
router.register(r'CotizacionVehiculo', CotizacionVehiculoViewSet, basename='CotizacionVehiculo')
router.register(r'Factura', FacturaViewSet, basename='Factura')
router.register(r'CategoriaInventario', CategoriaInventarioViewSet, basename='CategoriaInventario')


urlpatterns = [
    path('', home, name='home'),
    path('aboutUs/', aboutUs, name='aboutUs'),
    path('adminpage/', adminpage, name='adminpage'),
    path('cambiar_idioma/<str:idioma>/', cambiar_idioma, name='cambiar_idioma'),
    path('sucursales/', sucursales, name='sucursales'),
    path('sucursales/edit_sucursal', edit_sucursal, name='edit_sucursal'),
    path('sucursales/delete_sucursal', delete_Sucursal, name='delete_sucursal'),
    path('crear_sucursal/', create_sucursal, name='create_sucursal'),
    path('users/', users, name='users'),
    path('users/signup/', signup, name='signup'),
    path('users/edit_user/', edit_usuario, name='edit_usuario'),
    path('users/delete_user/', delete_Usuario, name='delete_user'),
    path('roles/', roles, name='roles'),
    path('roles/create_rol/', create_rol, name='new_rol'),
    path('roles/edit_rol/', edit_rol, name='edit_rol'),
    path('roles/delete_rol/', delete_rol, name='delete_rol'),
    path('inventory/', inventory, name='inventory'),
    path('inventory/create_product/', create_product, name='new_product'),
    path('inventory/create_vehicle/', create_vehiculoVenta, name='new_vehicle'),
    path('inventory/view_vehicule/', view_vehicle, name='vehicle_inventory'),
    path('inventory/edit_product/', edit_product, name='edit_product'),
    path('inventory/delete_product/', delete_product, name='delete_product'),
    path('inventory/delete_vehicle/', delete_vehiculoventa, name='delete_vehicle'),
    path('orders/', orders, name='orders'),
    ###
    path('orders/edit_order', edit_order, name='edit_order'),
    path('orders/delete_order', delete_order, name='delete_order'),
    ###
    path('orders/cerrar_orden', cerrar_orden_trabajo, name='cerrar_orden_trabajo'),
    path('orders/create_order', create_order, name='create_order'),
    path('cotizaciones/', cotizaciones, name='cotizaciones'),
    path('cotizaciones/cambiar_estado_cotizacion', cambiar_estado_cotizacion, name='cambiar_estado_cotizacion'),
    path('cotizaciones/edit_reparacion', edit_cotizacion_reparacion, name='edit_cotizacion_reparacion'),
    path('cotizaciones/delete_COTreparacion', delete_CotizacionReparacion, name='delete_CotizacionReparacion'),
    path('cotizaciones/cotizar_reparacion', create_CotizacionReparacion, name='cotizacion_reparacion'),
    path('sales/', sales, name='sales'),
    path('consulta_reparacion/', consulta_reparacion_cliente, name='consulta_reparacion_cliente'),
    path('reports/', reports, name='reports'),
    path('logout/', exit, name='exit'),
    path('appmanager/login_user/', login_user, name='login'),
    path('i18n/', include('django.conf.urls.i18n')),

    # ENRUTAMIENTO API
    path("api/", include(router.urls) ),
    # Documentacion Api
    path('docs/', include_docs_urls(title="How to Use API")),

]
