from flask import jsonify
import bcrypt
import logging
from models.entities.Usuario import Usuario

class ModelUser():
    
    @classmethod
    def login(cls,mysql,email,password):
        logger = logging.getLogger("LoginModule")
        try:
            logger.info(f"Iniciado proceso login para:\n email = {email} password = {password}")
            con = mysql.connect()
            cursor = con.cursor()
            cursor.execute(
<<<<<<< HEAD
                'SELECT usuarios.id, usuarios.nombre, usuarios.email, usuarios.idOrganizacion,  GROUP_CONCAT(roles.nombre) AS roles, usuarios.password ' + 
                'FROM usuarios ' +
                'INNER JOIN usuario_roles ON usuarios.id = usuario_roles.idUsuario ' +
                'INNER JOIN roles ON usuario_roles.idRol = roles.id ' +
                'WHERE usuarios.email = %s GROUP BY usuarios.id'
=======
                'select usuarios.id, usuarios.nombre, usuarios.email, usuarios.idOrganizacion, roles.nombre, usuarios.password ' + 
                'from usuarios ' +
                'inner join usuario_roles on usuarios.id = usuario_roles.idUsuario ' +
                'inner join roles on usuario_roles.idRol = roles.id ' +
                'where usuarios.email = %s'
>>>>>>> parent of a0dd29a (02/07)
                , (email)
            )
            row = cursor.fetchone()
            logger.warning(f"Datos recuperados:\n id = {row[0]} nombre = {row[1]} email = {row[2]} organizacion = {row[3]} rol = {row[4]} password = {row[5]}")
            isValidPassword = bcrypt.checkpw(password.encode('utf-8'), row[5].encode('utf-8'))
            logger.warning(f"Validación = {isValidPassword}")
            if isValidPassword:
                logger.info("Inicio de sesión correcto")
                usuario = Usuario(row[0],row[1],row[2],True,row[3],row[4])
                return usuario.to_dict()
            else:
                logger.warning("Email o contraseña incorrectos")
                return jsonify({'error': 'Email o contraseña incorrectos'}), 401
        except Exception as e:
            logger.error(f"Excepción: {e}")
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            con.close()
        
    
    @classmethod
    def getAllUsers(cls,mysql, org):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
<<<<<<< HEAD
            cursor.execute("SELECT usuarios.id, usuarios.nombre, usuarios.email, GROUP_CONCAT(roles.nombre) AS roles  FROM usuarios "+
                'INNER JOIN usuario_roles ON usuarios.id = usuario_roles.idUsuario ' +
                'INNER JOIN roles ON usuario_roles.idRol = roles.id ' +
                'WHERE idOrganizacion = ' + org +
                ' GROUP BY usuarios.id')
=======
            cursor.execute("select usuarios.id, usuarios.nombre, usuarios.email, roles.nombre  from usuarios "+
                'inner join usuario_roles on usuarios.id = usuario_roles.idUsuario ' +
                'inner join roles on usuario_roles.idRol = roles.id ' +
                'where idOrganizacion = ' + org)
>>>>>>> parent of a0dd29a (02/07)
            
            usuarios = cursor.fetchall()
            users= []
            
            for usuario in usuarios:
                user = Usuario(usuario[0],usuario[1],usuario[2],True,org,usuario[3])
                users.append(user.to_dict())
                
            return users
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getUsuariosPagina(cls,mysql, org, limit, offset):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
<<<<<<< HEAD
            cursor.execute(""" SELECT usuarios.id, usuarios.nombre, usuarios.email,  GROUP_CONCAT(roles.nombre) AS roles  FROM usuarios 
                INNER JOIN usuario_roles ON usuarios.id = usuario_roles.idUsuario
                INNER JOIN roles ON usuario_roles.idRol = roles.id
                WHERE idOrganizacion = %s GROUP BY usuarios.id ORDER BY id ASC LIMIT %s OFFSET %s""", (org, limit, offset))
=======
            cursor.execute(""" select usuarios.id, usuarios.nombre, usuarios.email, roles.nombre  from usuarios 
                inner join usuario_roles on usuarios.id = usuario_roles.idUsuario
                inner join roles on usuario_roles.idRol = roles.id
                where idOrganizacion = %s order by id ASC limit %s offset %s""", (org, limit, offset))
>>>>>>> parent of a0dd29a (02/07)
            
            usuarios = cursor.fetchall()
            users= []
            
            for usuario in usuarios:
                user = Usuario(usuario[0],usuario[1],usuario[2],True,org,usuario[3])
                users.append(user.to_dict())
                
            return users
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def getUsuario(cls,mysql,usuarioId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
<<<<<<< HEAD
            cursor.execute("SELECT usuarios.id, usuarios.nombre, usuarios.email, usuarios.idOrganizacion, GROUP_CONCAT(roles.nombre) AS roles  FROM usuarios "+
                'INNER JOIN usuario_roles ON usuarios.id = usuario_roles.idUsuario ' +
                'INNER JOIN roles ON usuario_roles.idRol = roles.id ' +
                'WHERE usuarios.id = ' + usuarioId +
                ' GROUP BY usuarios.id')
=======
            cursor.execute("select usuarios.id, usuarios.nombre, usuarios.email, usuarios.idOrganizacion, roles.nombre  from usuarios "+
                'inner join usuario_roles on usuarios.id = usuario_roles.idUsuario ' +
                'inner join roles on usuario_roles.idRol = roles.id ' +
                'where usuarios.id = ' + usuarioId)
>>>>>>> parent of a0dd29a (02/07)
            
            row = cursor.fetchone()
            if row != None:
                usuario = Usuario(row[0],row[1],row[2],True,row[3],row[4])
                return usuario.to_dict()
            
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()
            
            
    @classmethod
    def createUser(cls,mysql, nombre, email, password, idOrganizacion, rol):
        try:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(4))
            
            conn = mysql.connect()
            cursor = conn.cursor()
            
            try:
                cursor.execute(
                    "INSERT INTO usuarios (nombre, email, password, idOrganizacion) VALUES(%s,%s,%s,%s)",
                    (nombre,email,hashed_password,idOrganizacion)
                )
                conn.commit()
                usuario_id = cursor.lastrowid
            except:
                return jsonify({'message': 'Error al crear el usuario'}), 400
            
<<<<<<< HEAD
            try:
                for rol in roles:        
                    cursor.execute(
                        "INSERT INTO usuario_roles (idUsuario, idRol) VALUES(%s,%s)",
                        (usuario_id,rol)
                    )
                    conn.commit()
=======
            try:        
                cursor.execute(
                    "insert into usuario_roles (idUsuario, idRol) values(%s,%s)",
                    (usuario_id,rol)
                )
                conn.commit()
>>>>>>> parent of a0dd29a (02/07)
            except:
                return jsonify({'message': 'Error al asignar rol'}), 400

            
            cursor.execute(
                'SELECT usuarios.id, usuarios.nombre, usuarios.email, usuarios.idOrganizacion, roles.nombre ' + 
                'FROM usuarios ' +
                'INNER JOIN usuario_roles ON usuarios.id = usuario_roles.idUsuario ' +
                'INNER JOIN roles ON usuario_roles.idRol = roles.id ' +
                'WHERE usuarios.id = %s'
                , (usuario_id)
            )
            
            row = cursor.fetchone()
            
            usuario = Usuario(row[0],row[1],row[2],True,row[3],row[4])
            
            
            return usuario.to_dict()
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def deleteUser(cls,mysql,usuarioId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            print("Eliminando usuario con ID:", usuarioId)
            cursor.execute("DELETE FROM paciente_personalreferencia WHERE idUsuario = %s", (usuarioId,))
            cursor.execute("DELETE FROM usuario_roles WHERE idUsuario = %s", (usuarioId,))
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuarioId,))
            print("Filas afectadas:", cursor.rowcount)
            conn.commit()
            print("Commit ejecutado correctamente")
            return jsonify({'ok':'ok'}), 200
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)}), 400
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def updateDataUser(cls,mysql,usuarioId, nombre, email, idOrganizacion, roles):
        try:
                        
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute(
                "update usuarios set nombre = %s, email = %s where id = %s",
                (nombre,email,usuarioId)
            )
            conn.commit()
            
            usuario = Usuario(usuarioId,nombre,email,True,idOrganizacion,roles)
            
            return usuario.to_dict()
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def updatePassword(cls,mysql,usuarioId, password):
        try:
            #password = '123456'
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(4))
            
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute(
                "UPDATE usuarios SET password = %s WHERE id = %s",
                (hashed_password,usuarioId)
            )
            conn.commit()
            
            return jsonify({'ok':'ok'}), 200
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def getUserByEmail(cls,mysql,email):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute("SELECT usuarios.id FROM usuarios WHERE usuarios.email = %s", (email))
            
            userId = cursor.fetchone()
                        
            if userId != None:
                return userId
            
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def getPersonalReferencia(cls,mysql,pacienteId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""
                           SELECT usuarios.nombre, roles.nombre FROM usuarios 
                           INNER JOIN paciente_personalReferencia ON usuarios.id = paciente_personalReferencia.idUsuario
                           INNER JOIN pacientes ON pacientes.id = paciente_personalReferencia.idPaciente INNER JOIN usuario_roles ON usuarios.id = usuario_roles.idUsuario
                           INNER JOIN roles ON usuario_roles.idRol = roles.id
                           WHERE pacientes.id = %s
                           """, (pacienteId))
            
            usuarios = cursor.fetchall()
            users= []
            
            for usuario in usuarios:
                user = Usuario("",usuario[0],"",True,"",usuario[1])
                users.append(user.to_dict())
                
            return users
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()