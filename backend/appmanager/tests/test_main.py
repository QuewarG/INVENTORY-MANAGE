from django.test import TestCase
from appmanager.models import (
    VehiculoVenta,
    Rol,
    RepuestoVenta,
    Cargo,
    CategoriaInventario,
)


class VehiculoVentaTest(TestCase):
    def test_crear_vehiculo_venta(self):

        vehiculo = VehiculoVenta.objects.create(
            vehvnt_placa="ABC123",
            vehvnt_marca="Toyota",
            vehvnt_modelo="Corolla",
            vehvnt_color="Rojo",
            vehvnt_anio="2022",
            vehvnt_precioneto=15000.00,
            vehvnt_disponible=True,
            vehvnt_vigente=True,
        )

        self.assertEqual(vehiculo.vehvnt_placa, "ABC123")
        self.assertEqual(vehiculo.vehvnt_marca, "Toyota")
        self.assertEqual(vehiculo.vehvnt_modelo, "Corolla")
        self.assertEqual(vehiculo.vehvnt_color, "Rojo")
        self.assertEqual(vehiculo.vehvnt_anio, "2022")
        self.assertEqual(vehiculo.vehvnt_precioneto, 15000.00)
        self.assertTrue(vehiculo.vehvnt_disponible)
        self.assertTrue(vehiculo.vehvnt_vigente)

        self.assertIsNotNone(vehiculo.pk)


class RolTest(TestCase):
    def test_crear_rol(self):
        rol = Rol.objects.create(
            rol_nombre="Administrador",
            rol_descripcion="Responsable de la administración del sistema",
            rol_vigente=True,
        )

        self.assertEqual(rol.rol_nombre, "Administrador")
        self.assertEqual(
            rol.rol_descripcion, "Responsable de la administración del sistema"
        )
        self.assertTrue(rol.rol_vigente)
        self.assertIsNotNone(rol.pk)

    def test_crear_rol_sin_descripcion(self):
        rol = Rol.objects.create(rol_nombre="Usuario", rol_vigente=True)

        self.assertEqual(rol.rol_nombre, "Usuario")
        self.assertIsNone(rol.rol_descripcion)
        self.assertTrue(rol.rol_vigente)
        self.assertIsNotNone(rol.pk)

    def test_obtener_codigo_rol(self):
        rol = Rol.objects.create(
            rol_nombre="Supervisor",
            rol_descripcion="Responsable de supervisar las operaciones",
            rol_vigente=True,
        )

        self.assertEqual(rol.obtener_codigo_rol(), rol.rol_cod)


class RepuestoVentaTest(TestCase):
    def test_crear_repuesto_venta(self):
        repuesto = RepuestoVenta.objects.create(
            repvnt_descripcion="Descripción del repuesto", repvnt_vigente=True
        )

        self.assertEqual(repuesto.repvnt_descripcion, "Descripción del repuesto")
        self.assertTrue(repuesto.repvnt_vigente)
        self.assertIsNotNone(repuesto.pk)

    def test_crear_repuesto_venta_sin_vigente(self):
        repuesto = RepuestoVenta.objects.create(
            repvnt_descripcion="Otra descripción de repuesto"
        )

        self.assertEqual(repuesto.repvnt_descripcion, "Otra descripción de repuesto")
        self.assertTrue(repuesto.repvnt_vigente)
        self.assertIsNotNone(repuesto.pk)


class CargoTest(TestCase):
    def test_crear_cargo(self):
        cargo = Cargo.objects.create(
            cargo_nombre="Gerente",
            cargo_descripcion="Responsable de la gestión de la empresa",
            cargo_vigente=True,
        )

        self.assertEqual(cargo.cargo_nombre, "Gerente")
        self.assertEqual(
            cargo.cargo_descripcion, "Responsable de la gestión de la empresa"
        )
        self.assertTrue(cargo.cargo_vigente)
        self.assertIsNotNone(cargo.pk)

    def test_crear_cargo_sin_vigente(self):
        cargo = Cargo.objects.create(
            cargo_nombre="Asistente",
            cargo_descripcion="Asiste en diversas tareas",
        )

        self.assertEqual(cargo.cargo_nombre, "Asistente")
        self.assertEqual(cargo.cargo_descripcion, "Asiste en diversas tareas")
        self.assertTrue(cargo.cargo_vigente)
        self.assertIsNotNone(cargo.pk)


class CategoriaInventarioTest(TestCase):
    def test_crear_categoria_inventario(self):
        categoria = CategoriaInventario.objects.create(
            categoriainv_nombre="Categoría de prueba", categoriainv_vigente=True
        )

        self.assertEqual(categoria.categoriainv_nombre, "Categoría de prueba")
        self.assertTrue(categoria.categoriainv_vigente)
        self.assertIsNotNone(categoria.pk)

    def test_crear_categoria_inventario_sin_vigente(self):
        categoria = CategoriaInventario.objects.create(
            categoriainv_nombre="Otra categoría de prueba"
        )

        self.assertEqual(categoria.categoriainv_nombre, "Otra categoría de prueba")
        self.assertTrue(categoria.categoriainv_vigente)
        self.assertIsNotNone(categoria.pk)
