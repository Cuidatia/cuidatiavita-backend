import datetime
class Paciente():
    def __init__(self, id: int, nombre: str, primerApellido: str, segundoApellido: str, alias: str, fechaNacimiento: str, direccion: str, localidad: str, nacionalidad: str, genero: str, estadoCivil: str, idOrganizacion: int, imgPerfil: str):
            self.id = id
            self.nombre = nombre
            self.primerApellido = primerApellido
            self.segundoApellido = segundoApellido
            self.alias = alias
            self.fechaNacimiento = fechaNacimiento
            self.direccion = direccion
            self.localidad = localidad
            self.nacionalidad = nacionalidad
            self.genero = genero
            self.estadoCivil = estadoCivil
            self.idOrganizacion = idOrganizacion
            self.imgPerfil = imgPerfil
        
    def to_dict(self): 
        return {
            'id' : self.id,
            'nombre': self.nombre,
            'primerApellido': self.primerApellido,
            'segundoApellido': self.segundoApellido,
            'alias': self.alias,
            'fechaNacimiento': self.fechaNacimiento.isoformat(),
            'direccion': self.direccion,
            'localidad': self.localidad,
            'nacionalidad': self.nacionalidad,
            'genero': self.genero,
            'estadoCivil': self.estadoCivil,
            'idOrganizacion': self.idOrganizacion,
            'imgPerfil': self.imgPerfil
        }