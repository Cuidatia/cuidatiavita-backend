from flask import jsonify
from .entities.Paciente import Paciente

class ModelPaciente():
    @classmethod
    def getPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            select * from pacientes where id = %s   
                        """, (idPaciente))
            
            row = cursor.fetchone()
            paciente= Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])

            return paciente.to_dict()
        except:
            return jsonify({'error':'Error al obtener el paciente.'})
        finally:
            cursor.close()
            conn.close()
        
        
    @classmethod
    def getPacientes(cls,mysql,idOrganizacion):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            select * from pacientes where idOrganizacion = %s   
                        """, (idOrganizacion))
            
            rows = cursor.fetchall()
            pacientes= []
            
            for row in rows:
                paciente = Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
                pacientes.append(paciente.to_dict())
                
            return pacientes
        except:
            return jsonify({'error':'Error al obtener los pacientes.'})
        finally:
            cursor.close()
            conn.close()
        
        
    @classmethod
    def createPaciente(cls,mysql,nombre,primerApellido,segundoApellido,alias,fechaNacimiento,direccion,localidad,nacionalidad,genero,estadoCivil,imgPerfil,idOrganizacion):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           insert into pacientes (nombre,primerApellido,segundoApellido,alias,fechaNacimiento,direccion,localidad,nacionalidad,genero,estadoCivil,imgPerfil,idOrganizacion)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (nombre,primerApellido,segundoApellido,alias,fechaNacimiento,direccion,localidad,nacionalidad,genero,estadoCivil,imgPerfil,idOrganizacion) )
            
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
        
    
    @classmethod
    def deletePaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            delete from pacientes where id = %s   
                        """, (idPaciente))
            
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()