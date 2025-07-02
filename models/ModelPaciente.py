from flask import jsonify
from .entities.Paciente import *

class ModelPaciente():
#####################################################################################
    @classmethod
    def getPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT * FROM pacientes WHERE id = %s """, (idPaciente))
            row = cursor.fetchone()
            paciente= Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],
                               row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18])
            return paciente.to_dict()
        except Exception as e:
            return jsonify({'error':'Error al obtener el paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def getPacienteName(cls, mysql, idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT name, firstSurname, secondSurname FROM pacientes WHERE id = %s""", (idPaciente,))
            row = cursor.fetchone()
            pacienteNombreCompleto = row[0] + ' ' + row[1] + ' ' + row[2]
            if row:
                return pacienteNombreCompleto
            else:
                return None
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def getPacientes(cls,mysql,idOrganizacion):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT * FROM pacientes WHERE idOrganizacion = %s """, (idOrganizacion))
            rows = cursor.fetchall()
            pacientes= []
            for row in rows:
                paciente = Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],
                                    row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18])
                pacientes.append(paciente.to_dict())
            return pacientes
        except Exception as e:
            print(e)
            return jsonify({'error':'Error al obtener los pacientes.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def getPacientesPagina(cls,mysql,idOrganizacion,limit, offSET):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT * FROM pacientes WHERE idOrganizacion = %s ORDER BY id ASC LIMIT %s OFFSET %s""", (idOrganizacion, limit, offSET))
            rows = cursor.fetchall()
            pacientes= []
            for row in rows:
                paciente = Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],
                                    row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18])
                pacientes.append(paciente.to_dict())
            return pacientes
        except:
            return jsonify({'error':'Error al obtener los pacientes.'})
        finally:
            cursor.close()
            conn.close()                               
    
    @classmethod
    def createPaciente(cls,mysql,idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,
                       nationality,gender,address,maritalStatus,sentimentalCouple,language,otherLanguages,culturalHeritage,faith):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           INSERT INTO pacientes (idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,
                           nationality,gender,address,maritalStatus,sentimentalCouple,language,otherLanguages,culturalHeritage,faith)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,
                                 nationality,gender,address,maritalStatus,sentimentalCouple,language,otherLanguages,culturalHeritage,faith))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updatePaciente(cls,mysql,idPaciente,idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,
                       nationality,gender,address,maritalStatus,sentimentalCouple,language,otherLanguages,culturalHeritage,faith):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE pacientes SET idOrganizacion = %s, name = %s, firstSurname = %s, secondSurname = %s, alias = %s,
                           birthDate = %s, age = %s, birthPlace = %s, nationality = %s, gender = %s, address = %s, maritalStatus = %s,
                           sentimentalCouple = %s, language = %s, otherLanguages = %s, culturalHeritage = %s, faith =%s WHERE id = %s
                           """, (idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,nationality,
                                 gender,address,maritalStatus,sentimentalCouple,language,otherLanguages,culturalHeritage,faith, idPaciente))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertPaciente(cls,mysql,idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,
                       nationality,gender,address,maritalStatus,sentimentalCouple,language,otherLanguages,culturalHeritage,faith,paciente_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM pacientes WHERE id = %s""", (paciente_id,))

            row = cursor.fetchone()
            if row is None:
                print('Create',row)
                # Create new paciente
            else:
                cls.updatePaciente(mysql,paciente_id,idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,nationality,gender,address,maritalStatus,sentimentalCouple,language,otherLanguages,culturalHeritage,faith)
                
            return jsonify({'okey': 'okey'}), 200
        except Exception as e:
            return jsonify({"error": "Error al buscar el paciente."}), 400
        finally:
            cursor.close()
            conn.close()
    
    @classmethod
    def deletePaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM pacientes WHERE id = %s """, (idPaciente))
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
            cursor.execute(""" SELECT * FROM lifestory WHERE idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            lifeStory= LifeStory(row[0],row[1])
            return lifeStory.to_dict()
        except:
            return jsonify({'error':'Error al obtener _lifeStory_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def createLifeStoryPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           INSERT INTO lifestory (idPaciente)
                            VALUES (%s)
                           """, (idPaciente))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteLifeStoryPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM lifestory WHERE idPaciente = %s """, (idPaciente))
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
            cursor.execute(""" SELECT * FROM mainSanitaryData WHERE idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            mainSanitaryData= MainSanitaryData(row[0],row[1],row[2],row[3],row[4])
            return mainSanitaryData.to_dict()
        except:
            return jsonify({'error':'Error al obtener _mainSanitaryData_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def createSanitaryDataPaciente(cls,mysql,idPaciente,mainIllness,allergies,otherIllness):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           INSERT INTO mainSanitaryData (idPaciente,mainIllness,allergies,otherIllness)
                            VALUES (%s,%s,%s,%s)
                           """, (idPaciente,mainIllness,allergies,otherIllness))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateSanitaryDataPaciente(cls,mysql,idPaciente,mainIllness,allergies,otherIllness):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE mainSanitaryData SET mainIllness = %s, allergies = %s, otherIllness = %s WHERE idPaciente = %s
                           """, (mainIllness,allergies,otherIllness,idPaciente))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteSanitaryDataPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM mainSanitaryData WHERE idPaciente = %s """, (idPaciente))
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
            cursor.execute(""" SELECT * FROM personality WHERE idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            personality= Personality(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10], row[11], row[12])
            return personality.to_dict()
        except Exception as e:
            return jsonify({'error':'Error al obtener _personality_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def createPersonalityPaciente(cls,mysql, pacienteId, nature, habits, likes, dislikes, calmMethods,disturbMethods,hobbies,technologyLevel,goals,favouriteSongs,clothes):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           INSERT INTO personality (idPaciente,nature,habits,likes,dislikes,calmMethods,disturbMethods,hobbies,technologyLevel,goals,favouriteSongs,clothes)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (pacienteId,nature,habits,likes,dislikes,calmMethods,disturbMethods,hobbies,technologyLevel,goals,favouriteSongs,clothes))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            print(e)
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updatePersonalityPaciente(cls,mysql,idPaciente,nature,habits,likes,dislikes,calmMethods,disturbMethods,hobbies,technologyLevel,goals,favouriteSongs,clothes):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE personality SET nature = %s, habits = %s, likes = %s, dislikes = %s, calmMethods = %s,
                           disturbMethods = %s, hobbies = %s, technologyLevel = %s, goals = %s, favouriteSongs = %s, clothes = %s WHERE idPaciente = %s
                           """, (nature,habits,likes,dislikes,calmMethods,disturbMethods,hobbies,technologyLevel,goals,favouriteSongs,clothes,idPaciente))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def upsertPersonalityPaciente(cls,mysql,idPaciente,nature,habits,likes,dislikes,calmMethods,disturbMethods,hobbies,technologyLevel,goals,favouriteSongs,clothes):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM personality WHERE idPaciente = %s""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createPersonalityPaciente(mysql,idPaciente,nature,habits,likes,dislikes,calmMethods,disturbMethods,hobbies,technologyLevel,goals,favouriteSongs,clothes)
            else:
                return cls.updatePersonalityPaciente(mysql,idPaciente,nature,habits,likes,dislikes,calmMethods,disturbMethods,hobbies,technologyLevel,goals,favouriteSongs,clothes)
        except Exception as e:
            return jsonify({"error": "Error al buscar la personalidad del paciente."}), 400
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deletePersonalityPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM personality WHERE idPaciente = %s """, (idPaciente))
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
            cursor.execute(""" SELECT * FROM contactData WHERE idPaciente = %s  """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            contactData= ContactData(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7], row[8], row[9])
            return contactData.to_dict()
        except Exception as e:
            print(e)
            return jsonify({'error':'Error al obtener _contactData_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def createContactDataPaciente(cls,mysql,idPaciente,contactName,contactFirstSurname,contactSecondSurname,contactAddress,contactEmail,contactTelecom, curatela, deFactoGuardian):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           INSERT INTO contactData (idPaciente,contactName,contactFirstSurname,contactSecondSurname,contactAddress,contactEmail,contactTelecom, curatela, deFactoGuardian)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idPaciente,contactName,contactFirstSurname,contactSecondSurname,contactAddress,contactEmail,contactTelecom, curatela, deFactoGuardian))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateContactDataPaciente(cls,mysql,idPaciente,contactName,contactFirstSurname,contactSecondSurname,contactAddress,contactEmail,contactTelecom, curatela, deFactoGuardian):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE contactData SET contactName = %s, contactFirstSurname = %s, contactSecondSurname = %s, contactAddress = %s, 
                           contactEmail = %s, contactTelecom = %s, curatela = %s, deFactoGuardian = %s WHERE idPaciente = %s
                           """, (contactName,contactFirstSurname,contactSecondSurname,contactAddress,contactEmail,contactTelecom,curatela, deFactoGuardian, idPaciente))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertContactDataPaciente(cls,mysql,idPaciente,contactName,contactFirstSurname,contactSecondSurname,contactAddress,contactEmail,contactTelecom, curatela, deFactoGuardian):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM contactData WHERE idPaciente = %s""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createContactDataPaciente(mysql,idPaciente,contactName,contactFirstSurname,contactSecondSurname,contactAddress,contactEmail,contactTelecom, curatela, deFactoGuardian)
            else:
                return cls.updateContactDataPaciente(mysql,idPaciente,contactName,contactFirstSurname,contactSecondSurname,contactAddress,contactEmail,contactTelecom, curatela, deFactoGuardian)
        except Exception as e:
            return jsonify({"error": "Error al buscar los datos de contacto del paciente."}), 400
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteContactDataPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM contactData WHERE idPaciente = %s """, (idPaciente))
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
            cursor.execute(""" SELECT * FROM images WHERE idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            images= Images(row[0],row[1],row[2],row[3])
            return images.to_dict()
        except:
            return jsonify({'error':'Error al obtener _images_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def createImagesPaciente(cls,mysql,idPaciente,photoReferences,photoCategory):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           INSERT INTO images (idPaciente,photoReferences,photoCategory)
                            VALUES (%s,%s,%s)
                           """, (idPaciente,photoReferences,photoCategory))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateImagesPaciente(cls,mysql,idPaciente,photoReferences,photoCategory):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE images SET photoReferences = %s, photoCategory = %s WHERE idPaciente = %s
                           """, (photoReferences,photoCategory,idPaciente))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteImagesPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM images WHERE idPaciente = %s """, (idPaciente))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getPharmacyPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT * FROM pharmacy
                           INNER JOIN mainSanitaryData ON mainSanitaryData.id = pharmacy.idSanitary
                           WHERE mainSanitaryData.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            pharmacy= Pharmacy(row[0],row[1],row[2],row[3],row[4],row[5])
            return pharmacy.to_dict()
        except:
            return jsonify({'error':'Error al obtener _pharmacy_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def createPharmacyPaciente(cls,mysql,idPaciente, treatment, regularPharmacy, visitFrequency, paymentMethod):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id FROM mainSanitaryData WHERE idPaciente = %s",(idPaciente))
            idSanitary = cursor.fetchone()
        except Exception as e:
            return e
        
        
        try:
            cursor.execute("""
                           INSERT INTO pharmacy (idSanitary, treatment, regularPharmacy, visitFrequency, paymentMethod)
                            VALUES (%s,%s,%s,%s,%s)
                           """, (idSanitary, treatment, regularPharmacy, visitFrequency, 'S'))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updatePharmacyPaciente(cls,mysql,idSanitary, treatment, regularPharmacy, visitFrequency, paymentMethod):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE pharmacy SET treatment = %s, regularPharmacy = %s, visitFrequency = %s, paymentMethod = %s WHERE idSanitary = %s
                           """, (treatment, regularPharmacy, visitFrequency, paymentMethod,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertPharmacyPaciente(cls,mysql,idPaciente, treatment, regularPharmacy, visitFrequency, paymentMethod):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM pharmacy WHERE idSanitary = %s""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createPharmacyPaciente(mysql,idPaciente, treatment, regularPharmacy, visitFrequency, paymentMethod)
            else:
                return cls.updatePharmacyPaciente(mysql,idPaciente, treatment, regularPharmacy, visitFrequency, paymentMethod)
        except Exception as e:
            return jsonify({"error": "Error al buscar la farmacia del paciente."}), 400
        finally:
            cursor.close()
            conn.close()
    
    @classmethod
    def deletePharmacyPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM pharmacy WHERE idSanitary = %s """, (idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getNursingPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT * FROM  nursingMedicine
                           INNER JOIN mainSanitaryData ON mainSanitaryData.id = nursingMedicine.idSanitary
                           WHERE mainSanitaryData.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            nursing = NursingMedicine(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            return nursing.to_dict()
        except:
            return jsonify({'error':'Error al obtener _nursingMedicine_ del paciente.'})
        finally:
            cursor.close()
            conn.close()      
    @classmethod
    def createNursingPaciente(cls,mysql,idPaciente,nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:

            cursor.execute("""
                           SELECT id FROM mainSanitaryData WHERE idPaciente = %s
                           """, (idPaciente))
            
            idSanitary = cursor.fetchone()

            cursor.execute("""
                           INSERT INTO nursingMedicine (idSanitary,nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences)
                            VALUES (%s,%s,%s,%s,%s,%s)
                           """, (idSanitary,nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateNursingPaciente(cls,mysql,idPaciente,nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           SELECT id FROM mainSanitaryData WHERE idPaciente = %s
                           """, (idPaciente))
            
            idSanitary = cursor.fetchone()

            cursor.execute("""
                           UPDATE nursingMedicine SET nutritionalSituation = %s, sleepQuality = %s, fallRisks = %s, mobilityNeeds = %s,
                           healthPreferences = %s WHERE idSanitary = %s
                           """, (nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertNursingPaciente(cls,mysql,idPaciente,nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM nursingMedicine WHERE idSanitary = %s""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createNursingPaciente(mysql,idPaciente,nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences)
            else:
                return cls.updateNursingPaciente(mysql,idPaciente,nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences)
        except Exception as e:
            return jsonify({"error": "Error al buscar la enfermería del paciente."}), 400
        finally:
            cursor.close()
            conn.close()
    
    @classmethod
    def deleteNursingPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM nursingMedicine WHERE idSanitary = %s """, (idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getSocialEdu(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT * FROM  socialEducationOccupationalTherapy
                           INNER JOIN mainSanitaryData ON mainSanitaryData.id =  socialEducationOccupationalTherapy.idSanitary
                           WHERE mainSanitaryData.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            socialEdu = SocialEducationOccupationalTherapy(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
            return socialEdu.to_dict()
        except:
            return jsonify({'error':'Error al obtener _socialEdu_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def createSocialEduPaciente(cls,mysql,idPaciente, cognitiveAbilities, affectiveCapacity, behaviorCapacity, collaborationLevel, autonomyLevel, groupParticipation):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           SELECT id FROM mainSanitaryData WHERE idPaciente = %s
                           """, (idPaciente))
            
            idSanitary = cursor.fetchone()
            
            cursor.execute("""
                           INSERT INTO  socialEducationOccupationalTherapy (idSanitary, cognitiveAbilities, affectiveCapacity, behaviorCapacity, collaborationLevel, autonomyLevel, groupParticipation)
                            VALUES (%s,%s,%s,%s, %s, %s, %s)
                           """, (idSanitary, cognitiveAbilities, affectiveCapacity, behaviorCapacity, collaborationLevel, autonomyLevel, groupParticipation))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            print(e)
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateSocialEduPaciente(cls,mysql,idSanitary, cognitiveAbilities, affectiveCapacity, behaviorCapacity, collaborationLevel, autonomyLevel, groupParticipation):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE  socialEducationOccupationalTherapy SET cognitiveAbilities = %s, affectiveCapacity = %s, behaviorCapacity = %s, collaborationLevel = %s, autonomyLevel = %s, groupParticipation = %s WHERE idSanitary = %s
                           """, (cognitiveAbilities, affectiveCapacity, behaviorCapacity,collaborationLevel, autonomyLevel, groupParticipation,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertSocialEduPaciente(cls,mysql,idPaciente, cognitiveAbilities, affectiveCapacity, behaviorCapacity, collaborationLevel, autonomyLevel, groupParticipation):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM socialEducationOccupationalTherapy WHERE idSanitary = %s""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createSocialEduPaciente(mysql,idPaciente, cognitiveAbilities, affectiveCapacity, behaviorCapacity, collaborationLevel, autonomyLevel, groupParticipation)
            else:
                return cls.updateSocialEduPaciente(mysql,idPaciente, cognitiveAbilities, affectiveCapacity, behaviorCapacity, collaborationLevel, autonomyLevel, groupParticipation)
        except Exception as e:
            return jsonify({"error": "Error al buscar la educación social del paciente."}), 400
        finally:
            cursor.close()
            conn.close()
    
    @classmethod
    def deleteSocialEduPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM  socialEducationOccupationalTherapy WHERE idSanitary = %s """, (idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getSocialWorkPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT socialWork.* FROM socialWork
                           INNER JOIN mainSanitaryData ON mainSanitaryData.id = socialWork.idSanitary
                           WHERE mainSanitaryData.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            socialWork= SocialWork(row[0],row[1],row[2],row[3],row[4],row[5])
            return socialWork.to_dict()
        except:
            return jsonify({'error':'Error al obtener _socialWork_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def createSocialWorkPaciente(cls,mysql,idPaciente, residentAndRelationship, petNameAndBreedPet, resources, legalSupport):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           SELECT id FROM mainSanitaryData WHERE idPaciente = %s
                           """, (idPaciente))
            
            idSanitary = cursor.fetchone()
            
            cursor.execute("""
                           INSERT INTO socialWork (idSanitary, residentAndRelationship, petNameAndBreedPet, resources, legalSupport)
                            VALUES (%s,%s,%s,%s,%s)
                           """, (idSanitary, residentAndRelationship, petNameAndBreedPet, resources, legalSupport))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateSocialWorkPaciente(cls,mysql,idSanitary, residentAndRelationship, petNameAndBreedPet, resources, legalSupport):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE socialWork SET residentAndRelationship = %s, petNameAndBreedPet = %s, resources = %s, legalSupport = %s WHERE idSanitary = %s
                           """, (residentAndRelationship,petNameAndBreedPet,resources,legalSupport,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertSocialWorkPaciente(cls,mysql,idPaciente, residentAndRelationship, petNameAndBreedPet, resources, legalSupport):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM socialWork WHERE idSanitary = %s""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createSocialWorkPaciente(mysql,idPaciente, residentAndRelationship, petNameAndBreedPet, resources, legalSupport)
            else:
                return cls.updateSocialWorkPaciente(mysql,idPaciente, residentAndRelationship, petNameAndBreedPet, resources, legalSupport)
        except Exception as e:
            return jsonify({"error": "Error al buscar el trabajo social del paciente."}), 400
        finally:
            cursor.close()
            conn.close()
    
    @classmethod
    def deleteSocialWorkPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM socialWork WHERE idSanitary = %s """, (idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getKitchenPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT * FROM kitchenHygiene
                           INNER JOIN mainSanitaryData ON mainSanitaryData.id = kitchenHygiene.idSanitary
                           WHERE mainSanitaryData.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            kitchen = KitchenHygiene(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            return kitchen.to_dict()
        except:
            return jsonify({'error':'Error al obtener _kitchenHygiene_ del paciente.'})
        finally:
            cursor.close()
            conn.close()      
    @classmethod
    def createKitchenPaciente(cls,mysql,idPaciente,favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT id FROM mainSanitaryData WHERE idPaciente = %s",(idPaciente))
            idSanitary = cursor.fetchone()
        except Exception as e:
            return e
        
        try:
            
            cursor.execute("""
                           INSERT INTO kitchenHygiene (idSanitary,favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan)
                            VALUES (%s,%s,%s,%s,%s,%s)
                           """, (idSanitary,favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            print(e)
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateKitchenPaciente(cls,mysql,idSanitary,favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE kitchenHygiene SET favouriteFood = %s, dietaryRestrictions = %s, confortAdvices = %s, routine = %s, carePlan = %s WHERE idSanitary = %s
                           """, (favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertKitchenPaciente(cls,mysql,idPaciente,favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM kitchenHygiene WHERE idSanitary = %s""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createKitchenPaciente(mysql,idPaciente,favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan)
            else:
                return cls.updateKitchenPaciente(mysql,idPaciente,favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan)
        except Exception as e:
            return jsonify({"error": "Error al buscar la cocina del paciente."}), 400
        finally:
            cursor.close()
            conn.close()        
            
    @classmethod
    def deleteKitchenPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM kitchenHygiene WHERE idSanitary = %s """, (idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getOtherDataPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT * FROM otherData
                           INNER JOIN mainSanitaryData ON mainSanitaryData.id = otherData.idSanitary
                           WHERE mainSanitaryData.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            otherData = OtherData(row[0],row[1],row[2])
            return otherData.to_dict()
        except:
            return jsonify({'error':'Error al obtener _otherData_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def createOtherDataPaciente(cls,mysql,idPaciente, professionalNotes):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT id FROM mainSanitaryData WHERE idPaciente = %s",(idPaciente))
            idSanitary = cursor.fetchone()
        except Exception as e:
            return e
        
        try:
            cursor.execute("""
                           INSERT INTO otherData (idSanitary, professionalNotes)
                            VALUES (%s,%s)
                           """, (idSanitary, professionalNotes))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateOtherDataPaciente(cls,mysql,idSanitary,professionalNotes):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE otherData SET professionalNotes = %s WHERE idSanitary = %s
                           """, (professionalNotes,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertOtherDataPaciente(cls,mysql,idPaciente,professionalNotes):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM otherData WHERE idSanitary = %s""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createOtherDataPaciente(mysql,idPaciente,professionalNotes)
            else:
                return cls.updateOtherDataPaciente(mysql,idPaciente,professionalNotes)
        except Exception as e:
            return jsonify({"error": "Error al buscar los otros datos del paciente."}), 400
        finally:
            cursor.close()
            conn.close()        
            
    @classmethod
    def deleteOtherDataPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM otherData WHERE idSanitary = %s """, (idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getChildhoodPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT * FROM childhood 
                           INNER JOIN lifeStory ON lifeStory.id = childhood.idLifeStory WHERE lifeStory.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            childhood = Childhood(row[0],row[1],row[2],row[3],row[4],row[5],row[6],
                                  row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15])
            return childhood.to_dict()
        except:
            return jsonify({'error':'Error al obtener _childhood_ del paciente.'})
        finally:
            cursor.close()
            conn.close() 
                   
    @classmethod
    def createChildhoodPaciente(cls,mysql,idPaciente,childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,
                                childhoodFriendsGroup, childhoodImportantPerson, childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                                childhoodNegativeExperiences, childhoodResponsabilities, childhoodAddress, childhoodLikes, childhoodAfraids):
        
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           SELECT id FROM lifestory WHERE idPaciente = %s
                           """, (idPaciente))
            
            idLifeStory = cursor.fetchone()
            print (idLifeStory)
            
            cursor.execute("""
                           INSERT INTO childhood (idLifeStory,childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,
                                childhoodFriendsGroup, childhoodImportantPerson, childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                                childhoodNegativeExperiences, childhoodResponsabilities, childhoodAddress, childhoodLikes, childhoodAfraids)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idLifeStory,childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,
                                childhoodFriendsGroup, childhoodImportantPerson, childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                                childhoodNegativeExperiences, childhoodResponsabilities, childhoodAddress, childhoodLikes, childhoodAfraids))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            print (e)
            raise e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def updateChildhoodPaciente(cls,mysql,idLifeStory,childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,
                                childhoodFriendsGroup, childhoodImportantPerson, childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                                childhoodNegativeExperiences, childhoodResponsabilities, childhoodAddress, childhoodLikes, childhoodAfraids):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE childhood SET childhoodStudies = %s, childhoodSchool = %s, childhoodMotivations = %s, childhoodFamilyCore = %s, childhoodFriendsGroup = %s, childhoodImportantPerson = %s,
                           childhoodTravels = %s, childhoodFavouritePlace = %s, childhoodPositiveExperiences = %s, childhoodNegativeExperiences = %s, childhoodResponsabilities = %s, childhoodAddress = %s, childhoodLikes = %s,
                           childhoodAfraids = %s WHERE idLifeStory = %s
                           """, (childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,childhoodFriendsGroup,childhoodImportantPerson,childhoodTravels,
                                 childhoodFavouritePlace, childhoodPositiveExperiences,childhoodNegativeExperiences, childhoodResponsabilities, childhoodAddress, 
                                 childhoodLikes, childhoodAfraids,idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertChildhoodPaciente(cls,mysql,idPaciente,childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,
                                childhoodFriendsGroup, childhoodImportantPerson, childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                                childhoodNegativeExperiences, childhoodResponsabilities, childhoodAddress, childhoodLikes, childhoodAfraids):
        conn = mysql.connect()
        cursor = conn.cursor()
        # try:
        cursor.execute("""SELECT COUNT(id) FROM childhood WHERE idLifeStory = (SELECT id FROM lifestory WHERE idPaciente = %s)""", (idPaciente,))
        row = cursor.fetchone()
        if row[0] == 0:
            return cls.createChildhoodPaciente(mysql,idPaciente,childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,
                            childhoodFriendsGroup, childhoodImportantPerson, childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                            childhoodNegativeExperiences, childhoodResponsabilities, childhoodAddress, childhoodLikes, childhoodAfraids)
        else:
            cursor.execute("""SELECT id FROM lifestory WHERE idPaciente = %s""", (idPaciente,))
            idLifeStory = cursor.fetchone()
            
            return cls.updateChildhoodPaciente(mysql,idLifeStory[0],childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,
                            childhoodFriendsGroup, childhoodImportantPerson, childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                            childhoodNegativeExperiences, childhoodResponsabilities, childhoodAddress, childhoodLikes, childhoodAfraids)
        # except Exception as e:
        #     return jsonify({"error": "Error al buscar la infancia del paciente."}), 400
            
    @classmethod
    def deleteChildhoodPaciente(cls,mysql,idLifeStory):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM childhood WHERE idLifeStory = %s """, (idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getYouthPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" SELECT * FROM youth 
                           INNER JOIN lifeStory ON lifeStory.id = youth.idLifeStory WHERE lifeStory.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            youth = Youth(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10], row[11],row[12],
                          row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21], row[22], row[23])
            return youth.to_dict()
        except:
            return jsonify({'error':'Error al obtener _youth_ del paciente.'})
        finally:
            cursor.close()
            conn.close()     
    @classmethod
    def createYouthPaciente(cls,mysql,idPaciente,youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,
                                youthFriendsGroup,youthImportantPerson,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthResponsabilities,youthAddress,youthLikes,youthHobbies,youthAfraids,youthSentimentalCouple,
                                youthProjects,youthUncompletedProjects, youthIllness, youthPersonalCrisis):
                                
        conn = mysql.connect()
        cursor = conn.cursor()
        try:

            cursor.execute("""
                            SELECT id FROM lifestory WHERE idPaciente = %s
                            """, (idPaciente))
            
            idLifeStory = cursor.fetchone()
        
            cursor.execute("""
                           INSERT INTO youth (idLifeStory,youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,
                                youthFriendsGroup,youthImportantPerson,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthResponsabilities,youthAddress,youthLikes,youthHobbies,youthAfraids,youthSentimentalCouple,
                                youthProjects,youthUncompletedProjects, youthIllness, youthPersonalCrisis)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idLifeStory,youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,
                                youthFriendsGroup,youthImportantPerson,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthResponsabilities,youthAddress,youthLikes,youthHobbies,youthAfraids,youthSentimentalCouple,
                                youthProjects,youthUncompletedProjects, youthIllness, youthPersonalCrisis))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateYouthPaciente(cls,mysql,idPaciente,youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,
                                youthFriendsGroup,youthImportantPerson,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthResponsabilities,youthAddress,youthLikes,youthHobbies,youthAfraids,youthSentimentalCouple,
                                youthProjects,youthUncompletedProjects, youthIllness, youthPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                            SELECT id FROM lifestory WHERE idPaciente = %s
                            """, (idPaciente))
            
            idLifeStory = cursor.fetchone()

            cursor.execute("""
                           UPDATE youth SET youthStudies = %s, youthSchool = %s, youthWorkPlace = %s, youthWorkRol = %s, youthFamilyCore = %s, youthFriendsGroup = %s, youthImportantPerson=%s,
                           youthTravels = %s, youthFavouritePlace = %s, youthRoutine = %s, youthPositiveExperiences = %s, youthNegativeExperiences = %s,youthResponsabilities = %s, youthAddress = %s,
                           youthLikes = %s,youthHobbies = %s,youthAfraids = %s,youthSentimentalCouple = %s,
                           youthProjects = %s,youthUncompletedProjects = %s,youthIllness = %s,youthPersonalCrisis = %s WHERE idLifeStory = %s
                           """, (youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,youthFriendsGroup,youthImportantPerson,youthTravels,youthFavouritePlace,youthRoutine,
                                youthPositiveExperiences,youthNegativeExperiences,youthResponsabilities,youthAddress,youthLikes,youthHobbies,youthAfraids,youthSentimentalCouple,youthProjects, youthUncompletedProjects, youthIllness,
                                youthPersonalCrisis,idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertYouthPaciente(cls,mysql,idPaciente,youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,
                                youthFriendsGroup,youthImportantPerson,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthResponsabilities,youthAddress,youthLikes,youthHobbies,youthAfraids,youthSentimentalCouple,youthProjects,
                                youthUncompletedProjects, youthIllness, youthPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM youth WHERE idLifeStory = (SELECT id FROM lifestory WHERE idPaciente = %s)""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createYouthPaciente(mysql,idPaciente,youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,
                                youthFriendsGroup,youthImportantPerson,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthResponsabilities,youthAddress,youthLikes,youthHobbies,youthAfraids,youthSentimentalCouple,youthProjects,
                                youthUncompletedProjects, youthIllness, youthPersonalCrisis)
            else:
                cursor.execute("""SELECT id FROM lifestory WHERE idPaciente = %s""", (idPaciente,))
                idLifeStory = cursor.fetchone()
                
                return cls.updateYouthPaciente(mysql,idLifeStory[0],youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,
                                youthFriendsGroup,youthImportantPerson,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthResponsabilities,youthAddress,youthLikes,youthHobbies,youthAfraids,youthSentimentalCouple,youthProjects,
                                youthUncompletedProjects, youthIllness, youthPersonalCrisis)
        except Exception as e:
            return jsonify({"error": "Error al buscar la juventud del paciente."}), 400
    
    @classmethod
    def deleteYouthPaciente(cls,mysql,idLifeStory):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM youth WHERE idLifeStory = %s """, (idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getAdulthoodPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute (""" SELECT * FROM adulthood
            INNER JOIN lifeStory ON lifeStory.id = adulthood.idLifeStory WHERE lifeStory.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            adulthood = Adulthood(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
                               row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22])
            return adulthood.to_dict()
        except:
            return jsonify({'error':'Error al obtener _adulthood_ del paciente.'})
        finally:
            cursor.close()
            conn.close()       
    @classmethod
    def createAdulthoodPaciente(cls,mysql,idPaciente,adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodImportantPerson,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodResponsabilities,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           SELECT id FROM lifestory WHERE idPaciente = %s
                           """, (idPaciente))
            
            idLifeStory = cursor.fetchone()
            print (idLifeStory)

            cursor.execute("""
                           INSERT INTO adulthood (idLifeStory,adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodImportantPerson,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodResponsabilities,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idLifeStory,adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodImportantPerson,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodResponsabilities,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateAdulthoodPaciente(cls,mysql,idPaciente,adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodImportantPerson,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodResponsabilities,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                            SELECT id FROM lifestory WHERE idPaciente = %s
                            """, (idPaciente))
            
            idLifeStory = cursor.fetchone()

            cursor.execute("""
                           UPDATE adulthood SET adulthoodSentimentalCouple = %s, adulthoodChildren = %s, adulthoodStudies = %s, adulthoodWorkPlace = %s, adulthoodWorkRol = %s,
                           adulthoodFamilyCore = %s, adulthoodFriendsGroup = %s, adulthoodWorkGroup = %s,adulthoodImportantPerson =%s,adulthoodTravels = %s, adulthoodFavouritePlace = %s, adulthoodRoutine = %s,
                           adulthoodPositiveExperiences = %s, adulthoodNegativeExperiences = %s,adulthoodResponsabilities=%s, adulthoodAddress = %s,adulthoodEconomicSituation = %s,adulthoodProjects = %s,
                           adulthoodUncompletedProjects = %s,adulthoodIllness = %s,adulthoodPersonalCrisis = %s WHERE idLifeStory = %s
                           """, (adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodImportantPerson,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodResponsabilities,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis,idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertAdulthoodPaciente(cls,mysql,idPaciente,adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodImportantPerson,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodResponsabilities,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM adulthood WHERE idLifeStory = (SELECT id FROM lifestory WHERE idPaciente = %s)""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createAdulthoodPaciente(mysql,idPaciente,adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodImportantPerson,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodResponsabilities,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis)
            else:
                cursor.execute("""SELECT id FROM lifestory WHERE idPaciente = %s""", (idPaciente,))
                idLifeStory = cursor.fetchone()
                
                return cls.updateAdulthoodPaciente(mysql,idLifeStory[0],adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodImportantPerson,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodResponsabilities,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis)
        except Exception as e:
            return jsonify({"error": "Error al buscar la adultez del paciente."}), 400
            
    @classmethod
    def deleteAdulthoodPaciente(cls,mysql,idLifeStory):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM adulthood WHERE idLifeStory = %s """, (idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
#####################################################################################
    @classmethod
    def getMaturityPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute (""" SELECT * FROM maturity
            INNER JOIN lifeStory ON lifeStory.id = maturity.idLifeStory WHERE lifeStory.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            maturity = Maturity(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
                               row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20])
            return maturity.to_dict()
        except Exception as e:
            print(e)
            return jsonify({'error':'Error al obtener _maturity_ del paciente.'})
        finally:
            cursor.close()
            conn.close()   
    @classmethod
    def createMaturityPaciente(cls,mysql,idPaciente,maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityImportantPerson,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityResponsabilities,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                            SELECT id FROM lifestory WHERE idPaciente = %s
                            """, (idPaciente))
            
            idLifeStory = cursor.fetchone()

            cursor.execute("""
                           INSERT INTO maturity (idLifeStory,maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityImportantPerson,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityResponsabilities,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idLifeStory,maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityImportantPerson,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityResponsabilities,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateMaturityPaciente(cls,mysql,idPaciente,maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityImportantPerson,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityResponsabilities,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                            SELECT id FROM lifestory WHERE idPaciente = %s
                            """, (idPaciente))
            
            idLifeStory = cursor.fetchone()

            cursor.execute("""
                           UPDATE maturity SET maturityGrandchildren = %s, maturityWorkPlace = %s, maturityWorkRol = %s, maturityFamilyCore = %s, maturityFriendsGroup = %s,
                           maturityWorkGroup = %s,maturityImportantPerson =%s, maturityTravels = %s, maturityFavouritePlace = %s, maturityRoutine = %s, maturityPositiveExperiences = %s, 
                           maturityNegativeExperiences = %s,maturityResponsabilities=%s, maturityRetirement = %s, maturityWills = %s, maturityProjects = %s,maturityUncompletedProjects = %s,
                           maturityIllness = %s,maturityPersonalCrisis = %s WHERE idLifeStory = %s
                           """, (maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityImportantPerson,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityResponsabilities,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis,idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def upsertMaturityPaciente(cls,mysql,idPaciente,maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityImportantPerson,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityResponsabilities,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT COUNT(id) FROM maturity WHERE idLifeStory = (SELECT id FROM lifestory WHERE idPaciente = %s)""", (idPaciente,))
            row = cursor.fetchone()
            if row[0] == 0:
                return cls.createMaturityPaciente(mysql,idPaciente,maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityImportantPerson,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityResponsabilities,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis)
            else:
                cursor.execute("""SELECT id FROM lifestory WHERE idPaciente = %s""", (idPaciente,))
                idLifeStory = cursor.fetchone()
                
                return cls.updateMaturityPaciente(mysql,idLifeStory[0],maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,
                                maturityFriendsGroup, maturityWorkGroup,maturityImportantPerson, maturityTravels, maturityFavouritePlace, maturityRoutine, 
                                maturityPositiveExperiences, maturityNegativeExperiences,maturityResponsabilities, maturityRetirement, maturityWills, 
                                maturityProjects, maturityUncompletedProjects, maturityIllness, maturityPersonalCrisis)
        except Exception as e:
            return jsonify({"error": "Error al buscar la madurez del paciente."}), 400
    
    @classmethod
    def deleteMaturityPaciente(cls,mysql,idLifeStory):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" DELETE FROM maturity WHERE idLifeStory = %s """, (idLifeStory))
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
                           SELECT * FROM pacientes 
                           INNER JOIN paciente_personalReferencia ON pacientes.id = paciente_personalReferencia.idPaciente
                           INNER JOIN usuarios ON usuarios.id = paciente_personalReferencia.idUsuario
                           WHERE usuarios.id = %s
                           """, (user))
            rows = cursor.fetchall()
            pacientes= []
            
            for row in rows:
                paciente = Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16], row[17])
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
                           INSERT INTO paciente_personalReferencia (idPaciente, idUsuario) 
                           VALUES (%s, %s)
                           """, (pacienteId, usuarioId))
            
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()

#####################################################################################   

    @classmethod
    def getAllPacientes(cls, mysql):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT pacientes.id, organizaciones.nombre, pacientes.name, pacientes.firstSurname, pacientes.secondSurname, pacientes.alias, pacientes.birthDate,
                pacientes.age, pacientes.birthPlace, pacientes.nationality, pacientes.gender, pacientes.address, pacientes.maritalStatus, pacientes.sentimentalCouple,
                pacientes.language, pacientes.otherLanguages, pacientes.culturalHeritage, pacientes.faith
                FROM pacientes
                INNER JOIN organizaciones ON pacientes.idOrganizacion = organizaciones.id
            """)
            rows = cursor.fetchall()
            pacientes = []

            for row in rows:
                paciente = Paciente(*row)
                
                childhood = cls.getChildhoodPaciente(mysql, row[0])
                youth = cls.getYouthPaciente(mysql,row[0])
                adulthood = cls.getAdulthoodPaciente(mysql, row[0])
                maturity = cls.getMaturityPaciente(mysql,row[0])
                
                
                lifestory = {
                    "childhood": childhood,
                    "youth": youth,
                    "adulthood": adulthood,
                    "maturity": maturity
                }
                
                pacientes.append({
                    **paciente.to_dict(),
                    "lifestory": lifestory
                })

            return pacientes
        except Exception as e:
            print(e)
            return e
        finally:
            cursor.close()
            conn.close()