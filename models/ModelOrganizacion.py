from flask import jsonify
from models.entities.Organizacion import Organizacion

class ModelOrganizacion():
    @classmethod
    def getOrganizacion(cls, mysql, id):
        
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM organizaciones WHERE id = %s", (id))
            row = cursor.fetchone()
            
            organizacion = Organizacion(row[0], row[1])
                    
            return organizacion.to_dict()
        
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getResumenOrganizacion(cls, mysql, id):
        
        conn = None
        cursor = None

        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute(""" select  gender, count(*) as cantidad from pacientes where idOrganizacion = %s group by gender """, (id,))
            desc = [col[0] for col in cursor.description]
            genero_data = [dict(zip(desc, row)) for row in cursor.fetchall()]
            total_usuarios = {"M": 0,"F": 0,"O": 0}
            for fila in genero_data:
                total_usuarios[fila['gender']] = fila['cantidad']
            
            cursor.execute(""" select count(distinct u.id) as total_profesionales from usuarios u inner join usuario_roles ur on u.id = ur.idUsuario
            where u.idOrganizacion = %s """, (id,))
            total_profesionales = cursor.fetchone()[0]

            cursor.execute(""" select r.nombre as rol, count(ur.idUsuario) as cantidad from usuario_roles ur inner join usuarios u on u.id = ur.idUsuario
            inner join roles r on r.id = ur.idRol where u.idOrganizacion = %s group by r.nombre order by cantidad DESC """, (id,))
            desc = [col[0] for col in cursor.description]
            total_roles = [dict(zip(desc, row)) for row in cursor.fetchall()]
                    
            return {"total_usuarios": total_usuarios, "total_profesionales": total_profesionales, "total_roles": total_roles}
        
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()