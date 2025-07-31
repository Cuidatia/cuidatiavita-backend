class Organizacion():
    def __init__(self, id, nombre, direccion, localidad, provincia, codigo_postal, telefono):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.provincia = provincia
        self.codigo_postal = codigo_postal
        self.telefono = telefono
        
    def to_dict(self):
        return {
            'id' : self.id,
            'nombre': self.nombre,
            'direccion' : self.direccion,
            'localidad' : self.localidad,
            'provincia' : self.provincia,
            'codigo_postal' : self.codigo_postal,
            'telefono' : self.telefono
        }
        