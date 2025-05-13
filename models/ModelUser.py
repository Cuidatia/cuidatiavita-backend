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
                'select usuarios.id, usuarios.nombre, usuarios.email, usuarios.idOrganizacion, roles.nombre, usuarios.password ' + 
                'from usuarios ' +
                'inner join usuario_roles on usuarios.id = usuario_roles.idUsuario ' +
                'inner join roles on usuario_roles.idRol = roles.id ' +
                'where usuarios.email = %s'
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
            
            cursor.execute("select usuarios.id, usuarios.nombre, usuarios.email, roles.nombre  from usuarios "+
                'inner join usuario_roles on usuarios.id = usuario_roles.idUsuario ' +
                'inner join roles on usuario_roles.idRol = roles.id ' +
                'where idOrganizacion = ' + org)
            
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
            
            cursor.execute("select usuarios.id, usuarios.nombre, usuarios.email, usuarios.idOrganizacion, roles.nombre  from usuarios "+
                'inner join usuario_roles on usuarios.id = usuario_roles.idUsuario ' +
                'inner join roles on usuario_roles.idRol = roles.id ' +
                'where usuarios.id = ' + usuarioId)
            
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
                    "insert into usuarios (nombre, email, password, idOrganizacion) values(%s,%s,%s,%s)",
                    (nombre,email,hashed_password,idOrganizacion)
                )
                conn.commit()
                usuario_id = cursor.lastrowid
            except:
                return jsonify({'message': 'Error al crear el usuario'}), 400
            
            try:        
                cursor.execute(
                    "insert into usuario_roles (idUsuario, idRol) values(%s,%s)",
                    (usuario_id,rol)
                )
                conn.commit()
            except:
                return jsonify({'message': 'Error al asignar rol'}), 400

            
            cursor.execute(
                'select usuarios.id, usuarios.nombre, usuarios.email, usuarios.idOrganizacion, roles.nombre ' + 
                'from usuarios ' +
                'inner join usuario_roles on usuarios.id = usuario_roles.idUsuario ' +
                'inner join roles on usuario_roles.idRol = roles.id ' +
                'where usuarios.id = %s'
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
            
            cursor.execute("delete from usuarios where id = %s", (usuarioId))
            conn.commit()
            
            return jsonify({'ok':'ok'}), 200
        except Exception as e:
            return jsonify({'error':e}), 400
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
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(4))
            
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute(
                "update usuarios set password = %s where id = %s",
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
            
            cursor.execute("select usuarios.id from usuarios where usuarios.email = %s", (email))
            
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
                           select usuarios.nombre from usuarios 
                           inner join paciente_personalReferencia on usuarios.id = paciente_personalReferencia.idUsuario
                           inner join pacientes on pacientes.id = paciente_personalReferencia.idPaciente
                           where pacientes.id = %s
                           """, (pacienteId))
            
            usuarios = cursor.fetchall()
            users= []
            
            for usuario in usuarios:
                user = Usuario("",usuario[0],"",True,"","")
                users.append(user.to_dict())
                
            return users
        except Exception as e:
            return jsonify({'error':e}), 400
        finally:
            cursor.close()
            conn.close()