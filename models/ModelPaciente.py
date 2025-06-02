from flask import jsonify
from .entities.Paciente import *

class ModelPaciente():
#####################################################################################
    @classmethod
    def getPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" select * from pacientes where id = %s """, (idPaciente))
            row = cursor.fetchone()
            paciente= Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],
                               row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16])
            return paciente.to_dict()
        except Exception as e:
            return jsonify({'error':'Error al obtener el paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def getPacientes(cls,mysql,idOrganizacion):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" select * from pacientes where idOrganizacion = %s """, (idOrganizacion))
            rows = cursor.fetchall()
            pacientes= []
            for row in rows:
                paciente = Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],
                                    row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16])
                pacientes.append(paciente.to_dict())
            return pacientes
        except:
            return jsonify({'error':'Error al obtener los pacientes.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def createPaciente(cls,mysql,idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,
                       nationality,gender,address,maritalStatus,language,otherLanguages,culturalHeritage,faith):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           insert into pacientes (idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,
                           nationality,gender,address,maritalStatus,language,otherLanguages,culturalHeritage,faith)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,
                                 nationality,gender,address,maritalStatus,language,otherLanguages,culturalHeritage,faith))
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
                       nationality,gender,address,maritalStatus,language,otherLanguages,culturalHeritage,faith):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           update pacientes set idOrganizacion = %s, name = %s, firstSurname = %s, secondSurname = %s, alias = %s,
                           birthDate = %s, age = %s, birthPlace = %s, nationality = %s, gender = %s, address = %s, maritalStatus = %s,
                           language = %s, otherLanguages = %s, culturalHeritage = %s, faith =%s where id = %s
                           """, (idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,nationality,
                                 gender,address,maritalStatus,language,otherLanguages,culturalHeritage,faith, idPaciente))
            conn.commit()
            return True
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
            cursor.execute(""" delete from pacientes where id = %s """, (idPaciente))
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
            cursor.execute(""" select * from lifestory where idPaciente = %s """, (idPaciente))
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
                           insert into lifestory (idPaciente)
                            values (%s)
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
            cursor.execute(""" delete from lifestory where idPaciente = %s """, (idPaciente))
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
            cursor.execute(""" select * from mainsanitarydata where idPaciente = %s """, (idPaciente))
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
                           insert into mainSanitaryData (idPaciente,mainIllness,allergies,otherIllness)
                            values (%s,%s,%s,%s)
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
                           update mainsanitarydata set mainIllness = %s, allergies = %s, otherIllness = %s where idPaciente = %s
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
            cursor.execute(""" delete from mainsanitarydata where idPaciente = %s """, (idPaciente))
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
            cursor.execute(""" select * from personality where idPaciente = %s """, (idPaciente))
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
                           insert into personality (idPaciente,nature,habits,likes,dislikes,calmMethods,disturbMethods,hobbies,technologyLevel,goals,favouriteSongs,clothes)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
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
                           update personality set nature = %s, habits = %s, likes = %s, dislikes = %s, calmMethods = %s,
                           disturbMethods = %s, hobbies = %s, technologyLevel = %s, goals = %s, favouriteSongs = %s, clothes = %s where idPaciente = %s
                           """, (nature,habits,likes,dislikes,calmMethods,disturbMethods,hobbies,technologyLevel,goals,favouriteSongs,clothes,idPaciente))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deletePersonalityPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from personality where idPaciente = %s """, (idPaciente))
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
            cursor.execute(""" select * from contactdata where idPaciente = %s  """, (idPaciente))
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
                           insert into contactdata (idPaciente,contactName,contactFirstSurname,contactSecondSurname,contactAddress,contactEmail,contactTelecom, curatela, deFactoGuardian)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s)
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
                           update contactdata set contactName = %s, contactFirstSurname = %s, contactSecondSurname = %s, contactAddress = %s, 
                           contactEmail = %s, contactTelecom = %s, curatela = %s, deFactoGuardian = %s where idPaciente = %s
                           """, (contactName,contactFirstSurname,contactSecondSurname,contactAddress,contactEmail,contactTelecom,curatela, deFactoGuardian, idPaciente))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteContactDataPaciente(cls,mysql,idPaciente):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from contactdata where idPaciente = %s """, (idPaciente))
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
            cursor.execute(""" select * from images where idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            images= Images(row[0],row[1],row[2])
            return images.to_dict()
        except:
            return jsonify({'error':'Error al obtener _images_ del paciente.'})
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def createImagesPaciente(cls,mysql,idPaciente,photoReferences):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           insert into images (idPaciente,photoReferences)
                            values (%s,%s)
                           """, (idPaciente,photoReferences))
            conn.commit()
            usuario_id = cursor.lastrowid
            return usuario_id
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def updateImagesPaciente(cls,mysql,idPaciente,photoReferences):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           update images set photoReferences = %s where idPaciente = %s
                           """, (photoReferences,idPaciente))
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
            cursor.execute(""" delete from images where idPaciente = %s """, (idPaciente))
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
            cursor.execute(""" select * from pharmacy
                           inner join mainSanitaryData on mainSanitaryData.id = pharmacy.idSanitary
                           where mainSanitaryData.idPaciente = %s """, (idPaciente))
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
            cursor.execute("select id from mainSanitaryData where idPaciente = %s",(idPaciente))
            idSanitary = cursor.fetchone()
        except Exception as e:
            return e
        
        
        try:
            cursor.execute("""
                           insert into pharmacy (idSanitary, treatment, regularPharmacy, visitFrequency, paymentMethod)
                            values (%s,%s,%s,%s,%s)
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
                           update pharmacy set treatment = %s, regularPharmacy = %s, visitFrequency = %s, paymentMethod = %s where idSanitary = %s
                           """, (treatment, regularPharmacy, visitFrequency, paymentMethod,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deletePharmacyPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from pharmacy where idSanitary = %s """, (idSanitary))
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
            cursor.execute(""" select * from  nursingmedicine
                           inner join mainSanitaryData on mainSanitaryData.id = nursingmedicine.idSanitary
                           where mainSanitaryData.idPaciente = %s """, (idPaciente))
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
                           select id from mainSanitaryData where idPaciente = %s
                           """, (idPaciente))
            
            idSanitary = cursor.fetchone()

            cursor.execute("""
                           insert into nursingmedicine (idSanitary,nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences)
                            values (%s,%s,%s,%s,%s,%s)
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
                           select id from mainSanitaryData where idPaciente = %s
                           """, (idPaciente))
            
            idSanitary = cursor.fetchone()

            cursor.execute("""
                           update nursingmedicine set nutritionalSituation = %s, sleepQuality = %s, fallRisks = %s, mobilityNeeds = %s,
                           healthPreferences = %s where idSanitary = %s
                           """, (nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteNursingPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from nursingmedicine where idSanitary = %s """, (idSanitary))
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
            cursor.execute(""" select * from socialeducationoccupationaltherapy
                           inner join mainSanitaryData on mainsanitaryData.id = socialeducationoccupationaltherapy.idSanitary
                           where mainsanitaryData.idPaciente = %s """, (idPaciente))
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
                           select id from mainSanitaryData where idPaciente = %s
                           """, (idPaciente))
            
            idSanitary = cursor.fetchone()
            
            cursor.execute("""
                           insert into socialeducationoccupationaltherapy (idSanitary, cognitiveAbilities, affectiveCapacity, behaviorCapacity, collaborationLevel, autonomyLevel, groupParticipation)
                            values (%s,%s,%s,%s, %s, %s, %s)
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
                           update socialeducationoccupationaltherapy set cognitiveAbilities = %s, affectiveCapacity = %s, behaviorCapacity = %s, collaborationLevel = %s, autonomyLevel = %s, groupParticipation = %s where idSanitary = %s
                           """, (cognitiveAbilities, affectiveCapacity, behaviorCapacity,collaborationLevel, autonomyLevel, groupParticipation,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteSocialEduPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from socialeducationoccupationaltherapy where idSanitary = %s """, (idSanitary))
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
            cursor.execute(""" select socialwork.* from socialwork
                           inner join mainSanitaryData on mainsanitaryData.id = socialwork.idSanitary
                           where mainsanitaryData.idPaciente = %s """, (idPaciente))
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
                           select id from mainSanitaryData where idPaciente = %s
                           """, (idPaciente))
            
            idSanitary = cursor.fetchone()
            
            cursor.execute("""
                           insert into socialwork (idSanitary, residentAndRelationship, petNameAndBreedPet, resources, legalSupport)
                            values (%s,%s,%s,%s,%s)
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
                           update socialwork set residentAndRelationship = %s, petNameAndBreedPet = %s, resources = %s, legalSupport = %s where idSanitary = %s
                           """, (residentAndRelationship,petNameAndBreedPet,resources,legalSupport,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteSocialWorkPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from socialwork where idSanitary = %s """, (idSanitary))
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
            cursor.execute(""" select * from kitchenhygiene
                           inner join mainSanitaryData on mainSanitaryData.id = kitchenHygiene.idSanitary
                           where mainSanitaryData.idPaciente = %s """, (idPaciente))
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
            cursor.execute("select id from mainSanitaryData where idPaciente = %s",(idPaciente))
            idSanitary = cursor.fetchone()
        except Exception as e:
            return e
        
        try:
            
            cursor.execute("""
                           insert into kitchenhygiene (idSanitary,favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan)
                            values (%s,%s,%s,%s,%s,%s)
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
                           update kitchenhygiene set favouriteFood = %s, dietaryRestrictions = %s, confortAdvices = %s, routine = %s, carePlan = %s where idSanitary = %s
                           """, (favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteKitchenPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from kitchenhygiene where idSanitary = %s """, (idSanitary))
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
            cursor.execute(""" select * from otherdata
                           inner join mainSanitaryData on mainSanitaryData.id = otherdata.idSanitary
                           where mainSanitaryData.idPaciente = %s """, (idPaciente))
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
            cursor.execute("select id from mainSanitaryData where idPaciente = %s",(idPaciente))
            idSanitary = cursor.fetchone()
        except Exception as e:
            return e
        
        try:
            cursor.execute("""
                           insert into otherdata (idSanitary, professionalNotes)
                            values (%s,%s)
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
                           update otherdata set professionalNotes = %s where idSanitary = %s
                           """, (professionalNotes,idSanitary))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteOtherDataPaciente(cls,mysql,idSanitary):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from otherdata where idSanitary = %s """, (idSanitary))
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
            cursor.execute(""" select * from childhood 
                           inner join lifeStory on lifeStory.id = childhood.idLifeStory where lifeStory.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            childhood = Childhood(row[0],row[1],row[2],row[3],row[4],row[5],row[6],
                                  row[7],row[8],row[9],row[10],row[11],row[12],row[13])
            return childhood.to_dict()
        except:
            return jsonify({'error':'Error al obtener _childhood_ del paciente.'})
        finally:
            cursor.close()
            conn.close() 
                   
    @classmethod
    def createChildhoodPaciente(cls,mysql,idPaciente,childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,
                                childhoodFriendsGroup,childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                                childhoodNegativeExperiences, childhoodAddress, childhoodLikes, childhoodAfraids):
        
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           select id from lifestory where idPaciente = %s
                           """, (idPaciente))
            
            idLifeStory = cursor.fetchone()
            print (idLifeStory)
            
            cursor.execute("""
                           insert into childhood (idLifeStory,childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,
                                childhoodFriendsGroup,childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                                childhoodNegativeExperiences, childhoodAddress, childhoodLikes, childhoodAfraids)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idLifeStory,childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,
                                childhoodFriendsGroup,childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                                childhoodNegativeExperiences, childhoodAddress, childhoodLikes, childhoodAfraids))
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
                                childhoodFriendsGroup,childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
                                childhoodNegativeExperiences, childhoodAddress, childhoodLikes, childhoodAfraids):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           update childhood set childhoodStudies = %s, childhoodSchool = %s, childhoodMotivations = %s, childhoodFamilyCore = %s, childhoodFriendsGroup = %s,
                           childhoodFavouritePlace = %s, childhoodPositiveExperiences = %s, childhoodNegativeExperiences = %s, childhoodAddress = %s, childhoodLikes = %s,
                           childhoodAfraids = %s where idLifeStory = %s
                           """, (childhoodStudies,childhoodSchool,childhoodMotivations,childhoodFamilyCore,childhoodFriendsGroup,childhoodTravels,
                                 childhoodFavouritePlace, childhoodPositiveExperiences,childhoodNegativeExperiences, childhoodAddress, 
                                 childhoodLikes, childhoodAfraids,idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteChildhoodPaciente(cls,mysql,idLifeStory):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from childhood where idLifeStory = %s """, (idLifeStory))
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
            cursor.execute(""" select * from youth 
                           inner join lifeStory on lifeStory.id = youth.idLifeStory where lifeStory.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            youth = Youth(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
                        row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20])
            return youth.to_dict()
        except:
            return jsonify({'error':'Error al obtener _youth_ del paciente.'})
        finally:
            cursor.close()
            conn.close()     
    @classmethod
    def createYouthPaciente(cls,mysql,idPaciente,youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,
                                youthFriendsGroup,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthAddress,youthLikes,youthHobbies,youthAfraids,youthProjects,
                                youthUncompletedProjects, youthIllness, youthPersonalCrisis):
                                
        conn = mysql.connect()
        cursor = conn.cursor()
        try:

            cursor.execute("""
                            select id from lifestory where idPaciente = %s
                            """, (idPaciente))
            
            idLifeStory = cursor.fetchone()
        
            cursor.execute("""
                           insert into youth (idLifeStory,youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,
                                youthFriendsGroup,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthAddress,youthLikes,youthHobbies,youthAfraids,youthProjects,
                                youthUncompletedProjects, youthIllness, youthPersonalCrisis)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idLifeStory,youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,
                                youthFriendsGroup,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthAddress,youthLikes,youthHobbies,youthAfraids,youthProjects,
                                youthUncompletedProjects, youthIllness, youthPersonalCrisis))
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
                                youthFriendsGroup,youthTravels,youthFavouritePlace,youthRoutine,youthPositiveExperiences,
                                youthNegativeExperiences,youthAddress,youthLikes,youthHobbies,youthAfraids,youthProjects,
                                youthUncompletedProjects, youthIllness, youthPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                            select id from lifestory where idPaciente = %s
                            """, (idPaciente))
            
            idLifeStory = cursor.fetchone()

            cursor.execute("""
                           update youth set youthStudies = %s, youthSchool = %s, youthWorkPlace = %s, youthWorkRol = %s, youthFamilyCore = %s, youthFriendsGroup = %s,
                           youthTravels = %s, youthFavouritePlace = %s, youthRoutine = %s, youthPositiveExperiences = %s, youthNegativeExperiences = %s, youthAddress = %s,
                           youthLikes = %s,youthHobbies = %s,youthAfraids = %s,youthProjects = %s,youthUncompletedProjects = %s,youthIllness = %s,youthPersonalCrisis = %s 
                           where idLifeStory = %s
                           """, (youthStudies,youthSchool,youthWorkPlace, youthWorkRol,youthFamilyCore,youthFriendsGroup,youthTravels,youthFavouritePlace,youthRoutine,
                                youthPositiveExperiences,youthNegativeExperiences,youthAddress,youthLikes,youthHobbies,youthAfraids,youthProjects, youthUncompletedProjects, youthIllness,
                                youthPersonalCrisis,idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteYouthPaciente(cls,mysql,idLifeStory):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from youth where idLifeStory = %s """, (idLifeStory))
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
            cursor.execute (""" select * from adulthood
            inner join lifeStory on lifeStory.id = adulthood.idLifeStory where lifeStory.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            adulthood = Adulthood(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
                               row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20])
            return adulthood.to_dict()
        except:
            return jsonify({'error':'Error al obtener _adulthood_ del paciente.'})
        finally:
            cursor.close()
            conn.close()       
    @classmethod
    def createAdulthoodPaciente(cls,mysql,idPaciente,adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           select id from lifestory where idPaciente = %s
                           """, (idPaciente))
            
            idLifeStory = cursor.fetchone()
            print (idLifeStory)

            cursor.execute("""
                           insert into adulthood (idLifeStory,adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idLifeStory,adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
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
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                            select id from lifestory where idPaciente = %s
                            """, (idPaciente))
            
            idLifeStory = cursor.fetchone()

            cursor.execute("""
                           update adulthood set adulthoodSentimentalCouple = %s, adulthoodChildren = %s, adulthoodStudies = %s, adulthoodWorkPlace = %s, adulthoodWorkRol = %s,
                           adulthoodFamilyCore = %s, adulthoodFriendsGroup = %s, adulthoodWorkGroup = %s, adulthoodTravels = %s, adulthoodFavouritePlace = %s, adulthoodRoutine = %s,
                           adulthoodPositiveExperiences = %s, adulthoodNegativeExperiences = %s, adulthoodAddress = %s,adulthoodEconomicSituation = %s,adulthoodProjects = %s,
                           adulthoodUncompletedProjects = %s,adulthoodIllness = %s,adulthoodPersonalCrisis = %s where idLifeStory = %s
                           """, (adulthoodSentimentalCouple,adulthoodChildren,adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol,adulthoodFamilyCore,
                                adulthoodFriendsGroup,adulthoodWorkGroup,adulthoodTravels,adulthoodFavouritePlace,adulthoodRoutine,adulthoodPositiveExperiences,
                                adulthoodNegativeExperiences,adulthoodAddress,adulthoodEconomicSituation,adulthoodProjects,adulthoodUncompletedProjects,
                                adulthoodIllness, adulthoodPersonalCrisis,idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteAdulthoodPaciente(cls,mysql,idLifeStory):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from adulthood where idLifeStory = %s """, (idLifeStory))
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
        print(idPaciente)
        try:
            cursor.execute (""" select * from maturity
            inner join lifeStory on lifeStory.id = maturity.idLifeStory where lifeStory.idPaciente = %s """, (idPaciente))
            row = cursor.fetchone()
            if row is None:
                return None
            maturity = Maturity(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
                               row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18])
            return maturity.to_dict()
        except Exception as e:
            print(e)
            return jsonify({'error':'Error al obtener _maturity_ del paciente.'})
        finally:
            cursor.close()
            conn.close()   
    @classmethod
    def createMaturityPaciente(cls,mysql,idPaciente,maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                            select id from lifestory where idPaciente = %s
                            """, (idPaciente))
            
            idLifeStory = cursor.fetchone()

            cursor.execute("""
                           insert into maturity (idLifeStory,maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                           """, (idLifeStory,maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
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
                                maturityWorkGroup,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                            select id from lifestory where idPaciente = %s
                            """, (idPaciente))
            
            idLifeStory = cursor.fetchone()

            cursor.execute("""
                           update maturity set maturityGrandchildren = %s, maturityWorkPlace = %s, maturityWorkRol = %s, maturityFamilyCore = %s, maturityFriendsGroup = %s,
                           maturityWorkGroup = %s, maturityTravels = %s, maturityFavouritePlace = %s, maturityRoutine = %s, maturityPositiveExperiences = %s, 
                           maturityNegativeExperiences = %s, maturityRetirement = %s, maturityWills = %s, maturityProjects = %s,maturityUncompletedProjects = %s,
                           maturityIllness = %s,maturityPersonalCrisis = %s where idLifeStory = %s
                           """, (maturityGrandchildren,maturityWorkPlace,maturityWorkRol,maturityFamilyCore,maturityFriendsGroup,
                                maturityWorkGroup,maturityTravels,maturityFavouritePlace,maturityRoutine,maturityPositiveExperiences,
                                maturityNegativeExperiences,maturityRetirement,maturityWills,maturityProjects,maturityUncompletedProjects,
                                maturityIllness,maturityPersonalCrisis,idLifeStory))
            conn.commit()
            return True
        except Exception as e:
            return e
        finally:
            cursor.close()
            conn.close()
    @classmethod
    def deleteMaturityPaciente(cls,mysql,idLifeStory):
        conn = mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(""" delete from maturity where idLifeStory = %s """, (idLifeStory))
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
                paciente = Paciente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16])
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