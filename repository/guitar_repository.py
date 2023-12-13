# guitar_repository.py
# from model.guitar_model import Guitar
from model.guitar_model import Guitar

class GuitarRepository:
    @staticmethod
    def get_all():
        return Guitar.query.all()

    @staticmethod
    def get_by_name(name):
        return Guitar.query.filter_by(name=name).first()