class Roles():
    def __init__(self, id: int, nombre: str, description: str):
        self.id = id
        self.nombre = nombre
        self.description = description
        
    def to_dict(self):
        return {
            'id' : self.id,
            'nombre': self.nombre,
            'description': self.description
        }