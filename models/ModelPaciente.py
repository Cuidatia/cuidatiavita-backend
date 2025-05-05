from flask import jsonify
from .entities.Paciente import *

class ModelPaciente():
#####################################################################################
    @classmethod
    def getPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            select * from pacientes where id = %s   
                        """, (idPaciente))
            
            row = cursor.fetchone()
            paciente= Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
                               row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21])

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
                paciente = Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
                                    row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21])
                pacientes.append(paciente.to_dict())
                
            return pacientes
        except:
            return jsonify({'error':'Error al obtener los pacientes.'})
        finally:
            cursor.close()
            conn.close()
        
        
    @classmethod
    def createPaciente(cls,mysql,idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,nationality,gender,
                       address,maritalStatus,language,otherLanguages,culturalHeritage,faith,lifeStory,personality,contactData,sanitary,images):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           insert into pacientes (idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,nationality,gender,
                           address,maritalStatus,language,otherLanguages.culturalHeritage,faith,lifeStory,personality,contactData,sanitary,images)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,nationality,gender,
                                 address,maritalStatus,language,otherLanguages,culturalHeritage,faith,lifeStory,personality,contactData,sanitary,images) )
            
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
#####################################################################################
    @classmethod
    def getLifeStoryPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            select * from lifestory where idPaciente = %s   
                        """, (idPaciente))
            
            row = cursor.fetchone()
            lifeStory= LifeStory(row[0],row[1],row[2],row[3],row[4],row[5])

            return lifeStory.to_dict()
        except:
            return jsonify({'error':'Error al obtener _lifeStory_ del paciente.'})
        finally:
            cursor.close()
            conn.close()  
        
    @classmethod
    def deleteLifeStoryPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            delete from lifestory where idPaciente = %s   
                        """, (idPaciente))
            
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getSanitaryDataPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            select * from mainsanitarydata where idPaciente = %s   
                        """, (idPaciente))
            
            row = cursor.fetchone()
            mainSanitaryData= MainSanitaryData(row[0],row[1],row[2],row[3],row[4])

            return mainSanitaryData.to_dict()
        except:
            return jsonify({'error':'Error al obtener _mainSanitaryData_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
    
    @classmethod
    def deleteSanitaryDataPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            delete from mainsanitarydata where idPaciente = %s   
                        """, (idPaciente))
            
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getPersonalityPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            select * from personality where idPaciente = %s   
                        """, (idPaciente))
            
            row = cursor.fetchone()
            personality= Personality(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])

            return personality.to_dict()
        except:
            return jsonify({'error':'Error al obtener _personality_ del paciente.'})
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def deletePersonalityPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            delete from personality where idPaciente = %s   
                        """, (idPaciente))
            
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getContactDataPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            select * from contactdata where idPaciente = %s   
                        """, (idPaciente))
            
            row = cursor.fetchone()
            contactData= ContactData(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])

            return contactData.to_dict()
        except:
            return jsonify({'error':'Error al obtener _contactData_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
        
    @classmethod
    def deleteContactDataPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            delete from contactdata where idPaciente = %s   
                        """, (idPaciente))
            
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getImagesPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            select * from images where idPaciente = %s   
                        """, (idPaciente))
            
            row = cursor.fetchone()
            images= Images(row[0],row[1],row[2])

            return images.to_dict()
        except:
            return jsonify({'error':'Error al obtener _images_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
        
    @classmethod
    def deleteImagesPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                            delete from images where idPaciente = %s   
                        """, (idPaciente))
            
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
            
    @classmethod
    def getPacientesReferencia(cls, mysql, user):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                           select * from pacientes 
                           inner join paciente_personalReferencia on pacientes.id = paciente_personalReferencia.idPaciente
                           inner join usuarios on usuarios.id = paciente_personalReferencia.idUsuario
                           where usuarios.id = %s
                           """, (user))
            rows = cursor.fetchall()
            pacientes= []
            
            for row in rows:
                paciente = Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
                pacientes.append(paciente.to_dict())
                
            return pacientes
        except Exception as e:
            return jsonify({'error':'Error al obtener los pacientes.'})
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def asignarPersonaReferencia(cls, mysql, pacienteId, usuarioId):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                           insert into paciente_personalReferencia (idPaciente, idUsuario) 
                           values (%s, %s)
                           """, (pacienteId, usuarioId))
            
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()