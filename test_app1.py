import unittest
from flask_testing import TestCase  # Importa la clase TestCase de flask_testing
from flask import Flask  # Importa la clase Flask de flask
from app import app  # Importa la instancia de la aplicación Flask desde app.py

# Define una clase de prueba que hereda de TestCase
class TestApp(TestCase):
    def create_app(self):
        # Configura la aplicación para pruebas
        app.config['TESTING'] = True  # Habilita el modo de prueba
        app.config['DEBUG'] = False  # Desactiva el modo de depuración
        return app  # Retorna la instancia configurada de la aplicación Flask

    # Define una prueba para el endpoint raíz "/"
    # esta prueba falla porque el código de estado es 400
    def test_root_endpoint(self):
        # Realiza una solicitud GET al endpoint raíz "/"
        response = self.client.get('/')
        # Verifica que el código de estado sea 200 y que el mensaje "Bienvenido" esté presente
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Bienvenido', response.data)

    # Define una prueba para el endpoint "/API/products"
    def test_get_products_endpoint(self):
        # Realiza una solicitud GET al endpoint "/API/products"
        response = self.client.get('/API/products')
        # Verifica que el código de estado sea 200
        self.assertEqual(response.status_code, 200)

    # Define una prueba para el endpoint "/API/products/NOMBRE"
    def test_get_product_by_name_endpoint(self):
        # Realiza una solicitud GET al endpoint "/API/products/Stratocaster"
        response = self.client.get('/API/products/Stratocaster')
        # Verifica que el código de estado sea 200
        self.assertEqual(response.status_code, 200)

# Ejecuta las pruebas si este script es ejecutado directamente
if __name__ == '__main__':
    unittest.main()
