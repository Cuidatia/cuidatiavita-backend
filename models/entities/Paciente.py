import datetime
class Paciente():
    def __init__(self, id: int, idOrganizacion: int, 
                 name: str, firstSurname: str, secondSurname: str, alias: str, birthDate: str, age : str, birthPlace: str, gender: str,
                 address: str, nationality: str, maritalStatus: str, language: str, otherLanguages: str, culturalHeritage : str, faith: str,
                 lifeStory = None, personality = None, contactData = None, sanitary = None, images = None):
            self.id = id
            self.idOrganizacion = idOrganizacion
            self.name = name
            self.firstSurname = firstSurname
            self.secondSurname = secondSurname
            self.alias = alias
            self.birthDate = birthDate
            self.age = age
            self.birthPlace = birthPlace
            self.nationality = nationality
            self.gender = gender
            self.address = address
            self.maritalStatus = maritalStatus
            self.language = language
            self.otherLanguages = otherLanguages
            self.culturalHeritage = culturalHeritage
            self.faith = faith
            self.lifeStory = lifeStory
            self.personality = personality
            self.contactData = contactData
            self.sanitary = sanitary
            self.images = images
    def to_dict(self): 
        return {
            'id' : self.id,
            'idOrganizacion': self.idOrganizacion,
            'name': self.name,
            'firstSurname': self.firstSurname,
            'secondSurname': self.secondSurname,
            'alias': self.alias,
            'birthDate': self.birthDate.isoformat(),
            'age' : self.age,
            'birthPlace' : self.birthPlace,
            'nationality': self.nationality,
            'gender' : self.gender,
            'address': self.address,
            'maritalStatus' : self.maritalStatus,
            'language': self.language,
            'otherLanguages' : self.otherLanguages,
            'culturalHeritage': self.culturalHeritage,
            'faith': self.faith,
            'lifeStory' : self.lifeStory.to_dict() if self.lifeStory else None,
            'personality' : self.personality.to_dict() if self.personality else None,
            'contactData' : self.contactData.to_dict() if self.contactData else None,
            'sanitary' : self.sanitary.to_dict() if self.sanitary else None,
            'images' : self.images.to_dict() if self.images else None
        }

class LifeStory():
     def __init__(self, id : int, idPaciente : int,
                  childhood = None, youth = None, adulthood = None, maturity = None):
          self.id = id
          self.idPaciente = idPaciente
          self.childhood = childhood
          self.youth = youth
          self.adulthood = adulthood
          self.maturity = maturity
     def to_dict(self): 
        return {
            'id' : self.id,
            'idPaciente' : self.idPaciente,
            'childhood' : self.childhood.to_dict() if self.childhood else None,
            'youth' : self.youth.to_dict() if self.youth else None,
            'adulthood' : self.adulthood.to_dict() if self.adulthood else None,
            'maturity' : self.maturity.to_dict() if self.maturity else None
        }

class Childhood():
     def __init__(self, id : int, idLifeStory : int,
                  childhoodStudy : str, childhoodSchool : str, childhoodMotivations : str, childhoodFamilyCore : str, childhoodFriendsGroup : str,
                  childhoodTravels : str, childhoodFavouritePlace : str, childhoodPositiveExperiences : str, childhoodNegativeExperiences : str,
                  childhoodAddress : str, childhoodLikes : str, childhoodAfraids : str):
          self.id = id
          self.idLifeStory = idLifeStory
          self.childhoodStudy = childhoodStudy
          self.childhoodSchool = childhoodSchool
          self.childhoodMotivations = childhoodMotivations
          self.childhoodFamilyCore = childhoodFamilyCore
          self.childhoodFriendsGroup = childhoodFriendsGroup
          self.childhoodTravels = childhoodTravels
          self.childhoodFavouritePlace = childhoodFavouritePlace
          self.childhoodPositiveExperiences = childhoodPositiveExperiences
          self.childhoodNegativeExperiences = childhoodNegativeExperiences
          self.childhoodAddress = childhoodAddress
          self.childhoodLikes = childhoodLikes
          self.childhoodAfraids = childhoodAfraids
     def to_dict(self): 
        return {
            'id' : self.id,
            'idLifeStory' : self.idLifeStory,
            'childhoodStudy' : self.childhoodStudy,
            'childhoodSchool' : self.childhoodSchool,
            'childhoodMotivations' : self.childhoodMotivations,
            'childhoodFamilyCore' : self.childhoodFamilyCore,
            'childhoodFriendsGroup' : self.childhoodFriendsGroup,
            'childhoodTravels' : self.childhoodTravels,
            'childhoodFavouritePlace' : self.childhoodFavouritePlace,
            'childhoodPositiveExperiences' : self.childhoodPositiveExperiences,
            'childhoodNegativeExperiences' : self.childhoodNegativeExperiences,
            'childhoodAddress' : self.childhoodAddress,
            'childhoodLikes' : self.childhoodLikes,
            'childhoodAfraids' : self.childhoodAfraids
        }
     
class Youth():
     def __init__(self, id : int, idLifeStory : int,
                  youthStudy : str, youthSchool : str, youthWorkplace : str, youthWorkRole : str, youthFamilyCore : str,
                  youthFriendsGroup : str, youthTravels : str, youthFavouritePlace : str, youthRoutine : str, youthPositiveExperiences : str, 
                  youthNegativeExperiences : str, youthAddress : str, youthLikes : str, youthHobby : str, youthAfraids : str,
                  youthProjects : str, youthUncompletedProjects : str, youthIllness : str, youthPersonalCrisis : str):
          self.id = id
          self.idLifeStory = idLifeStory
          self.youthStudy = youthStudy
          self.youthSchool = youthSchool
          self.youthWorkplace = youthWorkplace
          self.youthWorkRole = youthWorkRole
          self.youthFamilyCore = youthFamilyCore
          self.youthFriendsGroup = youthFriendsGroup
          self.youthTravels = youthTravels
          self.youthFavouritePlace = youthFavouritePlace
          self.youthRoutine = youthRoutine
          self.youthPositiveExperiences = youthPositiveExperiences
          self.youthNegativeExperiences = youthNegativeExperiences
          self.youthAddress = youthAddress
          self.youthLikes = youthLikes
          self.youthHobby = youthHobby
          self.youthAfraids = youthAfraids
          self.youthProjects = youthProjects
          self.youthUncompletedProjects = youthUncompletedProjects
          self.youthIllness = youthIllness
          self.youthPersonalCrisis = youthPersonalCrisis
     def to_dict(self): 
        return {
            'id' : self.id,
            'idLifeStory' : self.idLifeStory,
            'youthStudy' : self.youthStudy,
            'youthSchool' : self.youthSchool,
            'youthWorkplace' : self.youthWorkplace,
            'youthWorkRole' : self.youthWorkRole,
            'youthFamilyCore' : self.youthFamilyCore,
            'youthFriendsGroup' : self.youthFriendsGroup,
            'youthTravels' : self.youthTravels,
            'youthFavouritePlace' : self.youthFavouritePlace,
            'youthRoutine' : self.youthRoutine,
            'youthPositiveExperiences' : self.youthPositiveExperiences,
            'youthNegativeExperiences' : self.youthNegativeExperiences,
            'youthAddress' : self.youthAddress,
            'youthLikes' : self.youthLikes,
            'youthHobby' : self.youthHobby,
            'youthAfraids' : self.youthAfraids,
            'youthProjects' : self.youthProjects,
            'youthUncompletedProjects' : self.youthUncompletedProjects,
            'youthIllness' : self.youthIllness,
            'youthPersonalCrisis' : self.youthPersonalCrisis
        }
     
class Adulthood():
     def __init__(self, id : int, idLifeStory : int,
                  sentimentalCoupleAdulthood : str, childrenAdulthood : str, adulthoodStudy : str, adulthoodWorkplace : str,
                  adulthoodWorkRole : str, adulthoodFamilyCore : str, adulthoodFriendsGroup : str, adulthoodWorkGroup : str,
                  adulthoodTravels : str, adulthoodFavouritePlace : str, adulthoodRoutine : str, adulthoodPositiveExperiences : str, 
                  adulthoodNegativeExperiences : str, adulthoodAddress : str, adulthoodEconomicSituation : str,
                  adulthoodProjects : str, adulthoodUncompletedProjects : str, adulthoodIllness : str, adulthoodPersonalCrisis : str):
          self.id = id
          self.idLifeStory = idLifeStory
          self.sentimentalCoupleAdulthood = sentimentalCoupleAdulthood
          self.childrenAdulthood = childrenAdulthood
          self.adulthoodStudy = adulthoodStudy
          self.adulthoodWorkplace = adulthoodWorkplace
          self.adulthoodWorkRole = adulthoodWorkRole
          self.adulthoodFamilyCore = adulthoodFamilyCore
          self.adulthoodFriendsGroup = adulthoodFriendsGroup
          self.adulthoodWorkGroup = adulthoodWorkGroup
          self.adulthoodTravels = adulthoodTravels
          self.adulthoodFavouritePlace = adulthoodFavouritePlace
          self.adulthoodRoutine = adulthoodRoutine
          self.adulthoodPositiveExperiences = adulthoodPositiveExperiences
          self.adulthoodNegativeExperiences = adulthoodNegativeExperiences
          self.adulthoodAddress = adulthoodAddress
          self.adulthoodEconomicSituation = adulthoodEconomicSituation
          self.adulthoodProjects = adulthoodProjects
          self.adulthoodUncompletedProjects = adulthoodUncompletedProjects
          self.adulthoodIllness = adulthoodIllness
          self.adulthoodPersonalCrisis = adulthoodPersonalCrisis
     def to_dict(self): 
        return {
            'id' : self.id,
            'idLifeStory' : self.idLifeStory,
            'sentimentalCoupleAdulthood' : self.sentimentalCoupleAdulthood,
            'childrenAdulthood' : self.childrenAdulthood,
            'adulthoodStudy' : self.adulthoodStudy,
            'adulthoodWorkplace' : self.adulthoodWorkplace,
            'adulthoodWorkRole' : self.adulthoodWorkRole,
            'adulthoodFamilyCore' : self.adulthoodFamilyCore,
            'adulthoodFriendsGroup' : self.adulthoodFriendsGroup,
            'adulthoodWorkGroup' : self.adulthoodWorkGroup,
            'adulthoodTravels' : self.adulthoodTravels,
            'adulthoodFavouritePlace' : self.adulthoodFavouritePlace,
            'adulthoodRoutine' : self.adulthoodRoutine,
            'adulthoodPositiveExperiences' : self.adulthoodPositiveExperiences,
            'adulthoodNegativeExperiences' : self.adulthoodNegativeExperiences,
            'adulthoodAddress' : self.adulthoodAddress,
            'adulthoodEconomicSituation' : self.adulthoodEconomicSituation,
            'adulthoodProjects' : self.adulthoodProjects,
            'adulthoodUncompletedProjects' : self.adulthoodUncompletedProjects,
            'adulthoodIllness' : self.adulthoodIllness,
            'adulthoodPersonalCrisis' : self.adulthoodPersonalCrisis
        }
     
class Maturity():
     def __init__(self, id : int, idLifeStory : int,
                  grandchildrenMaturity : str, maturityWorkplace : str, maturityWorkRole : str, maturityFamilyCore : str,
                  maturityFriendsGroup : str, maturityWorkGroup : str, maturityTravels : str, maturityFavouritePlace : str,
                  maturityRoutine : str, maturityPositiveExperiences : str, maturityNegativeExperiences : str,
                  maturityRetirement : str, maturityWills : str, maturityProjects : str, maturityUncompletedProjects : str,
                  maturityIllness : str, maturityPersonalCrisis : str):
          self.id = id
          self.idLifeStory = idLifeStory
          self.grandchildrenMaturity = grandchildrenMaturity
          self.maturityWorkplace = maturityWorkplace
          self.maturityWorkRole = maturityWorkRole
          self.maturityFamilyCore = maturityFamilyCore
          self.maturityFriendsGroup = maturityFriendsGroup
          self.maturityWorkGroup = maturityWorkGroup
          self.maturityTravels = maturityTravels
          self.maturityFavouritePlace = maturityFavouritePlace
          self.maturityRoutine = maturityRoutine
          self.maturityPositiveExperiences = maturityPositiveExperiences
          self.maturityNegativeExperiences = maturityNegativeExperiences
          self.maturityRetirement = maturityRetirement
          self.maturityWills = maturityWills
          self.maturityProjects = maturityProjects
          self.maturityUncompletedProjects = maturityUncompletedProjects
          self.maturityIllness = maturityIllness
          self.maturityPersonalCrisis = maturityPersonalCrisis
     def to_dict(self): 
        return {
            'id' : self.id,
            'idLifeStory' : self.idLifeStory,
            'grandchildrenMaturity' : self.grandchildrenMaturity,
            'maturityWorkplace' : self.maturityWorkplace,
            'maturityWorkRole' : self.maturityWorkRole,
            'maturityFamilyCore' : self.maturityFamilyCore,
            'maturityFriendsGroup' : self.maturityFriendsGroup,
            'maturityWorkGroup' : self.maturityWorkGroup,
            'maturityTravels' : self.maturityTravels,
            'maturityFavouritePlace' : self.maturityFavouritePlace,
            'maturityRoutine' : self.maturityRoutine,
            'maturityPositiveExperiences' : self.maturityPositiveExperiences,
            'maturityNegativeExperiences' : self.maturityNegativeExperiences,
            'maturityRetirement' : self.maturityRetirement,
            'maturityWills' : self.maturityWills,
            'maturityUncompletedProjects' : self.maturityUncompletedProjects,
            'maturityUncompletedProjects' : self.maturityUncompletedProjects,
            'maturityIllness' : self.maturityIllness,
            'maturityPersonalCrisis' : self.maturityPersonalCrisis
        }

class Personality():
     def __init__(self, id : int, idPaciente : int,
                  nature : str, habits : str, likes : str, dislikes : str, calmMethods : str, disturbMethods : str, hobby : str,
                  tecnologyLevel : str, goals : str):
          self.id = id
          self.idPaciente = idPaciente
          self.nature = nature
          self.habits = habits
          self.likes = likes
          self.dislikes = dislikes
          self.calmMethods = calmMethods
          self.disturbMethods = disturbMethods
          self.hobby = hobby
          self.tecnologyLevel = tecnologyLevel
          self.goals = goals
     def to_dict(self): 
        return {
          'id' : self.id,
          'idPaciente' : self.idPaciente,
          'nature' : self.nature,
          'habits' : self.habits,
          'likes' : self.likes,
          'dislikes' : self.dislikes,
          'calmMethods' : self.calmMethods,
          'disturbMethods' : self.disturbMethods,
          'hobby' : self.hobby,
          'tecnologyLevel' : self.tecnologyLevel,
          'goals' : self.goals
        }
     
class ContactData():
     def __init__(self, id : int, idPaciente : int,
                  contactName : str, contactFirstName : str, contactSecondSurname : str, contactAddress : str, contactEmail : str, contactTelecom : str):
          self.id = id
          self.idPaciente = idPaciente
          self.contactName = contactName
          self.contactFirstSurname = contactFirstName
          self.contactSecondSurname = contactSecondSurname
          self.contactAddress = contactAddress
          self.contactEmail = contactEmail
          self.contactTelecom = contactTelecom
     def to_dict(self): 
        return {
            'id' : self.id,
            'idPaciente' : self.idPaciente,
            'contactName' : self.contactName,
            'contactFirstSurname' : self.contactFirstSurname,
            'contactSecondSurname' : self.contactSecondSurname,
            'contactAddress' : self.contactAddress,
            'contactEmail' : self.contactEmail,
            'contactTelecom' : self.contactTelecom
        }
     
class MainSanitaryData():
     def __init__(self, id : int, idPaciente : int, 
                  mainIllness : str, allergies : str, otherIllness : str,
                  pharmacy = None, nursing = None, socialEdu = None, socialWork = None, kitchen = None, other = None):
          self.id = id
          self.idPaciente = idPaciente
          self.mainIllness = mainIllness
          self.allergies = allergies
          self.otherIllness = otherIllness
          self.pharmacy = pharmacy
          self.nursing = nursing
          self.socialEdu = socialEdu
          self.socialWork = socialWork
          self.kitchen = kitchen
          self.other = other

     def to_dict(self): 
        return {
            'id' : self.id,
            'idPaciente' : self.idPaciente,
            'mainIllness' : self.mainIllness,
            'allergies' : self.allergies,
            'otherIllness' : self.otherIllness,
            'pharmacy' : self.pharmacy.to_dict() if self.pharmacy else None,
            'nursing' : self.nursing.to_dict() if self.nursing else None,
            'socialEdu' : self.socialEdu.to_dict() if self.socialEdu else None,
            'socialWork' : self.socialWork.to_dict() if self.socialWork else None,
            'kitchen' : self.kitchen.to_dict() if self.kitchen else None,
            'other' : self.other.to_dict() if self.other else None
        }
     
class Pharmacy():
     def __init__(self, id : int, idSanitary: int,
                  treatment : str, regularPharmacy : str, visitFrequency : str, paymentMethod : str):
          self.id = id
          self.idSanitary = idSanitary
          self.treatment = treatment
          self.regularPharmacy = regularPharmacy
          self.visitFrequency = visitFrequency
          self.paymentMethod = paymentMethod
     def to_dict(self): 
        return {
            'id' : self.id,
            'idSanitary' : self.idSanitary,
            'treatment' : self.treatment,
            'regularPharmacy' : self.regularPharmacy,
            'visitFrequency' : self.visitFrequency,
            'paymentMethod' : self.paymentMethod
        }
     
class NursingMedicine():
     def __init__(self, id : int, idSanitary: int,
                  weight : int, height : int, nutritionalSituation : str, sleepQuality : str, fallRisks : str, mobilityNeeds : str, healthPreferences : str):
          self.id = id
          self.idSanitary = idSanitary
          self.weight = weight
          self.height = height
          self.nutritionalSituation = nutritionalSituation
          self.sleepQuality = sleepQuality
          self.fallRisks = fallRisks
          self.mobilityNeeds = mobilityNeeds
          self.healthPreferences = healthPreferences
     def to_dict(self): 
        return {
            'id' : self.id,
            'idSanitary' : self.idSanitary,
            'weight' : self.weight,
            'height' : self.height,
            'nutritionalSituation' : self.nutritionalSituation,
            'sleepQuality' : self.sleepQuality,
            'fallRisks' : self.fallRisks,
            'mobilityNeeds' : self.mobilityNeeds,
            'healthPreferences' : self.healthPreferences
        }
     
class SocialEducationOccupationalTherapy():
     def __init__(self, id : int, idSanitary: int,
                  cognitiveAbilities : str, affectiveCapacity : str, behaviourCapacity : str):
          self.id = id
          self.idSanitary = idSanitary
          self.cognitiveAbilities = cognitiveAbilities
          self.affectiveCapacity = affectiveCapacity
          self.behaviourCapacity = behaviourCapacity
     def to_dict(self): 
        return {
            'id' : self.id,
            'idSanitary' : self.idSanitary,
            'cognitiveAbilities' : self.cognitiveAbilities,
            'affectiveCapacity' : self.affectiveCapacity,
            'behaviourCapacity' : self.behaviourCapacity
        }

class SocialWork():
     def __init__(self, id : int, idSanitary: int,
                  residentAndRelationship : str, petNameAndBreetPet : str, collaborationLevel : str, autonomyLevel : str, groupParticipation : str, resources : str, legalSupport : str):
          self.id = id
          self.idSanitary = idSanitary
          self.residentAndRelationship = residentAndRelationship
          self.petNameAndBreetPet = petNameAndBreetPet
          self.collaborationLevel = collaborationLevel
          self.autonomyLevel = autonomyLevel
          self.groupParticipation = groupParticipation
          self.resources = resources
          self.legalSupport = legalSupport
     def to_dict(self): 
        return {
            'id' : self.id,
            'idSanitary' : self.idSanitary,
            'residentAndRelationship' : self.residentAndRelationship,
            'petNameAndBreetPet' : self.petNameAndBreetPet,
            'collaborationLevel' : self.collaborationLevel,
            'autonomyLevel' : self.autonomyLevel,
            'groupParticipation' : self.groupParticipation,
            'resources' : self.resources,
            'legalSupport' : self.legalSupport
        }
     
class KitchenHygiene():
     def __init__(self, id : int, idSanitary: int,
                  favouriteFood : str, dietaryRestrictions : str, confortAdvices : str, routine : str, carePlan : str):
          self.id = id
          self.idSanitary = idSanitary
          self.favouriteFood = favouriteFood
          self.dietaryRestrictions = dietaryRestrictions
          self.confortAdvices = confortAdvices
          self.routine = routine
          self.carePlan = carePlan
     def to_dict(self): 
        return {
            'id' : self.id,
            'idSanitary' : self.idSanitary,
            'favouriteFood' : self.favouriteFood,
            'dietaryRestrictions' : self.dietaryRestrictions,
            'confortAdvices' : self.confortAdvices,
            'routine' : self.routine,
            'carePlan' : self.carePlan
        }
     
class OtherData():
     def __init__(self, id : int, idSanitary: int,
                  professionalNotes : str):
          self.id = id
          self.idSanitary = idSanitary
          self.professionalNotes = professionalNotes
     def to_dict(self): 
        return {
            'id' : self.id,
            'idSanitary' : self.idSanitary,
            'professionalNotes' : self.professionalNotes
        }
     
class Images():
     def __init__(self, id : int, idPaciente : int,
                  photoReferences : str):
          self.id = id
          self.idPaciente = idPaciente
          self.photoReferences = photoReferences
     def to_dict(self): 
        return {
            'id' : self.id,
            'idPaciente' : self.idPaciente,
            'photoReferences' : self.photoReferences
        }