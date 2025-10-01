from flask import jsonify
import bcrypt

class Usuario():
    def __init__(self, id, nombre, email, password, idOrganizacion, roles, idTelegram=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.idOrganizacion = idOrganizacion
        self.roles = roles
        self.idTelegram = idTelegram
    def to_dict(self):
        return {
            'id' : self.id,
            'nombre': self.nombre,
            'email': self.email,
            'idOrganizacion': self.idOrganizacion,
            'roles': self.roles,
            'idTelegram' : self.idTelegram
        }
        
    @classmethod
    def validar_password(self,password):
        if len(password) < 8:
            return jsonify({'error':'La contraseña debe tener al menos 8 caracteres'}), 400