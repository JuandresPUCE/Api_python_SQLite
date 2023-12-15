import unittest
from flask import Flask
from app import app


# Define una clase de prueba que hereda de unittest.TestCase
class TestApp(unittest.TestCase):
    def setUp(self):
        # Configura la aplicación para pruebas
        app.config['TESTING'] = True  # Habilita el modo de prueba
        app.config['DEBUG'] = False  # Desactiva el modo de depuración
        self.app = app.test_client()  # Crea un cliente de prueba para la aplicación

    # Define una prueba para el endpoint raíz "/"
    def test_root_endpoint(self):
        # Realiza una solicitud GET al endpoint raíz "/"
        response = self.app.get('/')
        # Verifica que el código de estado sea 200 y que el mensaje "Bienvenido" esté presente
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenido', response.data)

    # Define una prueba para el endpoint "/API/products"
    def test_get_products_endpoint(self):
        # Realiza una solicitud GET al endpoint "/API/products"
        response = self.app.get('/API/products')
        # Verifica que el código de estado sea 200
        self.assertEqual(response.status_code, 200)

    # Define una prueba para el endpoint "/API/products/NOMBRE"
    def test_get_product_by_name_endpoint(self):
        # Realiza una solicitud GET al endpoint "/API/products/Stratocaster"
        response = self.app.get('/API/products/Stratocaster')
        # Verifica que el código de estado sea 200
        self.assertEqual(response.status_code, 200)

# Ejecuta las pruebas si este script es ejecutado directamente
if __name__ == '__main__':
    unittest.main()
