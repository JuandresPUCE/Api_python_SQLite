import unittest
from flask_testing import TestCase
from flask import Flask
from app import app

class TestApp(TestCase):
    def create_app(self):
        # Configurar la aplicación para pruebas
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        return app

    def test_root_endpoint(self):
        # Prueba el endpoint raíz
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenido', response.data)

    def test_get_products_endpoint(self):
        # Prueba el endpoint /API/products
        response = self.client.get('/API/products')
        self.assertEqual(response.status_code, 200)
        # Agrega más aserciones según la respuesta esperada

    def test_get_product_by_name_endpoint(self):
        # Prueba el endpoint /API/products/NOMBRE
        response = self.client.get('/API/products/Stratocaster')
        self.assertEqual(response.status_code, 200)
        # Agrega más aserciones según la respuesta esperada

if __name__ == '__main__':
    unittest.main()
