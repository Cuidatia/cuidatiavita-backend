from flask import jsonify
from models.entities.Organizacion import Organizacion

class ModelOrganizacion():

    @classmethod
    def getAllOrganizaciones(cls,mysql):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute("SELECT *  FROM organizaciones")
            
            organizaciones = cursor.fetchall()
            orgs= []
            
            for organizacion in organizaciones:
                org = Organizacion(organizacion[0],organizacion[1],organizacion[2],organizacion[3],organizacion[4],organizacion[5], organizacion[6])
                orgs.append(org.to_dict())
                
            return orgs
        except Exception as e:
            print(e)
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getAllOrganizacionesPagina(cls,mysql, limit, offset):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute(""" SELECT *  FROM organizaciones ORDER BY id ASC LIMIT %s OFFSET %s""", (limit, offset))
            
            organizaciones = cursor.fetchall()
            orgs= []
            
            for organizacion in organizaciones:
                org = Organizacion(organizacion[0],organizacion[1],organizacion[2],organizacion[3],organizacion[4],organizacion[5], organizacion[6])
                orgs.append(org.to_dict())
                
            return orgs
        except Exception as e:
            print(e)
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getOrganizacion(cls, mysql, id):
        
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM organizaciones WHERE id = %s", (id,))
            row = cursor.fetchone()

            if not row:
                return None
            
            organizacion = Organizacion(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    
            return organizacion.to_dict()
        
        except Exception as e:
            raise Exception(str(e))
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getResumenOrganizacion(cls, mysql, id, is_superadmin):
        
        conn = None
        cursor = None

        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
            if is_superadmin:
                cursor.execute("""SELECT gender, COUNT(*) AS cantidad FROM pacientes GROUP BY gender""")
            else:
                cursor.execute("""SELECT gender, COUNT(*) AS cantidad FROM pacientes WHERE idOrganizacion = %s GROUP BY gender""", (id,))
            desc = [col[0] for col in cursor.description]
            genero_data = [dict(zip(desc, row)) for row in cursor.fetchall()]
            total_usuarios = {"M": 0,"F": 0,"O": 0}
            for fila in genero_data:
                total_usuarios[fila['gender']] = fila['cantidad']
                
            if is_superadmin:
                cursor.execute("""SELECT COUNT(*) AS count_usuarios FROM pacientes WHERE time_added_paciente >= NOW() - INTERVAL 30 DAY""")
            else:
                cursor.execute("""SELECT COUNT(*) AS count_usuarios FROM pacientes WHERE idOrganizacion = %s AND time_added_paciente >= NOW() - INTERVAL 30 DAY""", (id,))
            count_usuarios = cursor.fetchone()
            
            if is_superadmin:
                cursor.execute("""SELECT COUNT(distinct u.id) AS total_profesionales FROM usuarios u INNER JOIN usuario_roles ur ON u.id = ur.idUsuario""")
            else:
                cursor.execute("""SELECT COUNT(distinct u.id) AS total_profesionales FROM usuarios u INNER JOIN usuario_roles ur ON u.id = ur.idUsuario WHERE u.idOrganizacion = %s""", (id,))
            total_profesionales = cursor.fetchone()[0]

            if is_superadmin:
                cursor.execute("""SELECT r.nombre AS rol, COUNT(ur.idUsuario) AS cantidad FROM usuario_roles ur INNER JOIN usuarios u ON u.id = ur.idUsuario INNER JOIN roles r ON r.id = ur.idRol GROUP BY r.nombre ORDER BY cantidad DESC""")
            else:
                cursor.execute("""SELECT r.nombre AS rol, COUNT(ur.idUsuario) AS cantidad FROM usuario_roles ur INNER JOIN usuarios u ON u.id = ur.idUsuario INNER JOIN roles r ON r.id = ur.idRol WHERE u.idOrganizacion = %s GROUP BY r.nombre ORDER BY cantidad DESC""", (id,))
            desc = [col[0] for col in cursor.description]
            total_roles = [dict(zip(desc, row)) for row in cursor.fetchall()]
                    
            return {"total_usuarios": total_usuarios, "total_profesionales": total_profesionales, "total_roles": total_roles, "usuarios_30_dias": count_usuarios}
        
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    @classmethod
    def createOrg(cls,mysql, nombre, direccion, localidad, provincia, codigo_postal, telefono):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
            try:
                cursor.execute(
                    "INSERT INTO organizaciones (nombre, direccion, localidad, provincia, codigo_postal, telefono) VALUES(%s,%s,%s,%s,%s,%s)",
                    (nombre,direccion, localidad, provincia, codigo_postal, telefono)
                )
                conn.commit()
                org_id = cursor.lastrowid
            except:
                return None
            
            cursor.execute(
                'SELECT id, nombre, direccion, localidad, provincia, codigo_postal, telefono ' + 
                'FROM organizaciones ' +
                'WHERE id = %s'
                , (org_id)
            )
            
            row = cursor.fetchone()
            
            organizacion = Organizacion(row[0],row[1],row[2],row[3],row[4],row[5], row[6])
            
            return organizacion.to_dict()
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def updateDataOrg(cls,mysql,organizacionId, nombre, direccion, localidad, provincia, codigo_postal, telefono):
        try:
                        
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute(
                "UPDATE organizaciones SET nombre = %s, direccion = %s, localidad = %s, provincia = %s, codigo_postal = %s, telefono = %s WHERE id = %s",
                (nombre, direccion, localidad, provincia, codigo_postal, telefono, organizacionId)
            )

            conn.commit()
            
            organizacion = Organizacion(organizacionId,nombre,direccion, localidad, provincia, codigo_postal, telefono)
            
            return organizacion.to_dict()
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def deleteOrg(cls, mysql, organizacionId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            print("Eliminando organizacion con ID:", organizacionId)

            cursor.execute("SELECT id FROM usuarios WHERE idOrganizacion = %s", (organizacionId,))
            usuarios = cursor.fetchall()

            if usuarios:
                usuario_ids = [str(u[0]) for u in usuarios]

                placeholders = ",".join(["%s"] * len(usuario_ids))

                cursor.execute(f"DELETE FROM paciente_personalreferencia WHERE idUsuario IN ({placeholders})", tuple(usuario_ids))
                cursor.execute(f"DELETE FROM usuario_roles WHERE idUsuario IN ({placeholders})", tuple(usuario_ids))
                cursor.execute(f"DELETE FROM usuarios WHERE id IN ({placeholders})", tuple(usuario_ids))

            cursor.execute("DELETE FROM organizaciones WHERE id = %s", (organizacionId,))

            conn.commit()
            print("Commit ejecutado correctamente")
            return True
        except Exception as e:
            print("Error eliminando organización:", e)
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()