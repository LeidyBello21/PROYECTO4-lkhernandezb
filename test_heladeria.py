import unittest
from models.producto import Helado
from models.heladeria import Heladeria
from models.base_complemento import Base, Complemento

class TestHeladeria(unittest.TestCase):

    def setUp(self):
        # Configuración previa a cada prueba
        ingredientes_base = [
            Base("Leche", 1000, 100, 40, "No Vegetariano", "Leche"),
            Base("Azúcar", 1000, 50, 30, "Vegetariano", "Dulce")
        ]
        productos = [
            Helado(nombre="Helado de Chocolate", precio=5.500, ingredientes=ingredientes_base),
            Helado(nombre="Helado de Vainilla", precio=4.500, ingredientes=ingredientes_base)
        ]
        self.heladeria = Heladeria(productos, ingredientes_base)

    def test_calcular_calorias(self):
        helado = self.heladeria.productos[0]
        self.assertEqual(helado.calcular_calorias(), 150)

    def test_calcular_costo(self):
        helado = self.heladeria.productos[0]
        self.assertEqual(helado.calcular_costo(), 2.0)

    def test_calcular_rentabilidad(self):
        helado = self.heladeria.productos[0]
        self.assertEqual(helado.calcular_rentabilidad(), 3.5)  # 5.500 - 2.0

    def test_producto_mas_rentable(self):
        helado = self.heladeria.productos[0]
        self.assertEqual(self.heladeria.producto_mas_rentable(), helado)

    def test_vender_producto_exitosa(self):
        mensaje = self.heladeria.vender("Helado de Chocolate")
        self.assertEqual(mensaje, "¡Vendido!")

    def test_vender_producto_fallido(self):
        # Cambiar inventario para que falle la venta
        ingrediente = self.heladeria.get_ingrediente_por_nombre("Leche")
        ingrediente.inventario = 0
        mensaje = self.heladeria.vender("Helado de Chocolate")
        self.assertEqual(mensaje, "¡Oh no! Nos hemos quedado sin Leche")

    def test_abastecer_ingrediente(self):
        # Suponiendo que 'Leche' es el primer ingrediente
        ingrediente = self.heladeria.get_ingrediente_por_nombre("Leche")
        ingrediente.abastecer(20)  # Aumentar el inventario de leche
        self.assertEqual(ingrediente.inventario, 120)  # Asegurarse que se actualizó correctamente

    def test_renovar_inventario_complementos(self):
      complemento = Complemento("Chispas de chocolate", 50, 10, True, es_vegetariano=True, es_extra=True)
      complemento.renovar_inventario(60)  # Asegúrate de que el inventario se actualice correctamente
      self.assertEqual(complemento.inventario, 60)

    def test_verificar_ingredientes(self):
        ingredientes = [Base("Leche", 1000, 100, 40, "No Vegetariano", "Leche")]
        self.assertTrue(self.heladeria.verificar_ingredientes(ingredientes))

    def test_reducir_inventario(self):
        ingredientes = [Base("Leche", 1000, 100, 40, "No Vegetariano", "Leche")]
        self.heladeria.reducir_inventario(ingredientes)
        # Verificar que el inventario se redujo correctamente
        ingrediente = self.heladeria.get_ingrediente_por_nombre("Leche")
        self.assertEqual(ingrediente.inventario, 99.8)

        
if __name__ == '__main__':
    unittest.main()
