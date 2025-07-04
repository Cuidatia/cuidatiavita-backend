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
            
            cursor.execute(""" SELECT  gender, COUNT(*) AS cantidad FROM pacientes WHERE idOrganizacion = %s GROUP BY gender """, (id,))
            desc = [col[0] for col in cursor.description]
            genero_data = [dict(zip(desc, row)) for row in cursor.fetchall()]
            total_usuarios = {"M": 0,"F": 0,"O": 0}
            for fila in genero_data:
                total_usuarios[fila['gender']] = fila['cantidad']
            
            cursor.execute(""" SELECT COUNT(distinct u.id) AS total_profesionales FROM usuarios u INNER JOIN usuario_roles ur ON u.id = ur.idUsuario
            WHERE u.idOrganizacion = %s """, (id,))
            total_profesionales = cursor.fetchone()[0]

            cursor.execute(""" SELECT r.nombre AS rol, COUNT(ur.idUsuario) AS cantidad FROM usuario_roles ur INNER JOIN usuarios u ON u.id = ur.idUsuario
            INNER JOIN roles r ON r.id = ur.idRol WHERE u.idOrganizacion = %s GROUP BY r.nombre ORDER BY cantidad DESC """, (id,))
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