# guitar_service.py
from repository.guitar_repository import GuitarRepository

class GuitarService:
    @staticmethod
    def get_all_guitars():
        return [guitar.serialize() for guitar in GuitarRepository.get_all()]

    @staticmethod
    def get_guitar_by_name(name):
        guitar = GuitarRepository.get_by_name(name)
        return guitar.serialize() if guitar else None