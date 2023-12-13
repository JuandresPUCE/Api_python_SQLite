#Data: "name": "Stratocaster","maker": "Fender","Type": "Bolt-on","price": 1500.00, "img": "https://www.fmicassets.com/Damroot/ZoomJpg/10010/0148020306_fen_ins_frt_1_rr.jpg"
#modelo primero
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Guitar(db.Model):
    __tablename__ = 'guitars'
    # atributos de la clase
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    maker = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    img = db.Column(db.String(500), nullable=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'maker': self.maker,
            'type': self.type,
            'price': self.price,
            'img': self.img
        }
