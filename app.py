from flask import Flask,jsonify, request
from model.guitar_model import db, Guitar
import os

app = Flask(__name__)
# Configuración de la base de datos
database_path = os.path.join(os.path.dirname(__file__), 'database', 'database.db')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
# Para que no salga un warning en la consola
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db.init_app(app)



# Definimos la ruta raíz ("/")
@app.route('/')
def root():
    # Cuando se accede a la ruta raíz, se devuelve un mensaje de bienvenida
    return "<h1>Bienvenido a la tienda de todo, digite /API/products para ver las guitarras disponibles</h1>"


# Definimos la ruta "/API/products"
from service.guitar_service import GuitarService

@app.route('/API/products')
def get_products():
    try:
        products = GuitarService.get_all_guitars()
        return jsonify(products)
    except Exception:
        return jsonify({"msg": "Error"}), 500
    
@app.route('/API/products/<string:name>')
def get_product(name):
    try:
        product = GuitarService.get_guitar_by_name(name)
        if product:
            return jsonify(product)
        else:
            return jsonify({"msg": "Guitar not found"}), 404
    except Exception:
        return jsonify({"msg": "Error"}), 500



# Si este script se ejecuta como el principal, iniciamos la aplicación Flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
