import datetime
class Paciente():
    def __init__(self, id: int, idOrganizacion: int, 
                 name: str, firstSurname: str, secondSurname: str, alias: str, birthDate: str, age : str, birthPlace: str, nationality: str, gender: str,
                 address: str, maritalStatus: str, sentimentalCouple: str, language: str, otherLanguages: str, culturalHeritage : str, faith: str, dataTelegram: str):
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
            self.sentimentalCouple = sentimentalCouple
            self.language = language
            self.otherLanguages = otherLanguages
            self.culturalHeritage = culturalHeritage
            self.faith = faith
            self.dataTelegram = dataTelegram
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
            'sentimentalCouple' : self.sentimentalCouple,
            'language': self.language,
            'otherLanguages' : self.otherLanguages,
            'culturalHeritage': self.culturalHeritage,
            'faith': self.faith,
            'dataTelegram' : self.dataTelegram
        }

class LifeStory():
     def __init__(self, id : int, idPaciente : int):
          self.id = id
          self.idPaciente = idPaciente
     def to_dict(self): 
        return {
            'id' : self.id,
            'idPaciente' : self.idPaciente
        }

class Childhood():
     def __init__(self, id : int, idLifeStory : int,
                  childhoodStudies : str, childhoodSchool : str, childhoodMotivations : str, childhoodFamilyCore : str, childhoodFriendsGroup : str, childhoodImportantPerson: str, 
                  childhoodTravels : str, childhoodFavouritePlace : str, childhoodPositiveExperiences : str, childhoodNegativeExperiences : str, childhoodResponsabilities: str,
                  childhoodAddress : str, childhoodLikes : str, childhoodAfraids : str, childhoodMusic: str):
          self.id = id
          self.idLifeStory = idLifeStory
          self.childhoodStudies = childhoodStudies
          self.childhoodSchool = childhoodSchool
          self.childhoodMotivations = childhoodMotivations
          self.childhoodFamilyCore = childhoodFamilyCore
          self.childhoodFriendsGroup = childhoodFriendsGroup
          self.childhoodImportantPerson = childhoodImportantPerson
          self.childhoodTravels = childhoodTravels
          self.childhoodFavouritePlace = childhoodFavouritePlace
          self.childhoodPositiveExperiences = childhoodPositiveExperiences
          self.childhoodNegativeExperiences = childhoodNegativeExperiences
          self.childhoodResponsabilities = childhoodResponsabilities
          self.childhoodAddress = childhoodAddress
          self.childhoodLikes = childhoodLikes
          self.childhoodAfraids = childhoodAfraids
          self.childhoodMusic = childhoodMusic
     def to_dict(self): 
        return {
            'id' : self.id,
            'idLifeStory' : self.idLifeStory,
            'childhoodStudies' : self.childhoodStudies,
            'childhoodSchool' : self.childhoodSchool,
            'childhoodMotivations' : self.childhoodMotivations,
            'childhoodFamilyCore' : self.childhoodFamilyCore,
            'childhoodFriendsGroup' : self.childhoodFriendsGroup,
            'childhoodImportantPerson' : self.childhoodImportantPerson,
            'childhoodTravels' : self.childhoodTravels,
            'childhoodFavouritePlace' : self.childhoodFavouritePlace,
            'childhoodPositiveExperiences' : self.childhoodPositiveExperiences,
            'childhoodNegativeExperiences' : self.childhoodNegativeExperiences,
            'childhoodResponsabilities' : self.childhoodResponsabilities,
            'childhoodAddress' : self.childhoodAddress,
            'childhoodLikes' : self.childhoodLikes,
            'childhoodAfraids' : self.childhoodAfraids,
            'childhoodMusic' : self.childhoodMusic
        }
     
class Youth():
     def __init__(self, id : int, idLifeStory : int,
                  youthStudies : str, youthSchool : str, youthWorkPlace : str, youthWorkRol : str, youthFamilyCore : str,
                  youthFriendsGroup : str, youthImportantPerson: str, youthTravels : str, youthFavouritePlace : str, youthRoutine : str, youthPositiveExperiences : str, 
                  youthNegativeExperiences : str, youthResponsabilities: str, youthAddress : str, youthLikes : str, youthHobbies : str, youthAfraids : str, youthSentimentalCouple: str,
                  youthProjects : str, youthUncompletedProjects : str, youthIllness : str, youthPersonalCrisis : str, youthMusic : str):
          self.id = id
          self.idLifeStory = idLifeStory
          self.youthStudies = youthStudies
          self.youthSchool = youthSchool
          self.youthWorkPlace = youthWorkPlace
          self.youthWorkRol = youthWorkRol
          self.youthFamilyCore = youthFamilyCore
          self.youthFriendsGroup = youthFriendsGroup
          self.youthImportantPerson = youthImportantPerson
          self.youthTravels = youthTravels
          self.youthFavouritePlace = youthFavouritePlace
          self.youthRoutine = youthRoutine
          self.youthPositiveExperiences = youthPositiveExperiences
          self.youthNegativeExperiences = youthNegativeExperiences
          self.youthResponsabilities = youthResponsabilities
          self.youthAddress = youthAddress
          self.youthLikes = youthLikes
          self.youthHobbies = youthHobbies
          self.youthAfraids = youthAfraids
          self.youthSentimentalCouple = youthSentimentalCouple
          self.youthProjects = youthProjects
          self.youthUncompletedProjects = youthUncompletedProjects
          self.youthIllness = youthIllness
          self.youthPersonalCrisis = youthPersonalCrisis
          self.youthMusic = youthMusic
     def to_dict(self): 
        return {
            'id' : self.id,
            'idLifeStory' : self.idLifeStory,
            'youthStudies' : self.youthStudies,
            'youthSchool' : self.youthSchool,
            'youthWorkPlace' : self.youthWorkPlace,
            'youthWorkRol' : self.youthWorkRol,
            'youthFamilyCore' : self.youthFamilyCore,
            'youthFriendsGroup' : self.youthFriendsGroup,
            'youthImportantPerson' : self.youthImportantPerson,
            'youthTravels' : self.youthTravels,
            'youthFavouritePlace' : self.youthFavouritePlace,
            'youthRoutine' : self.youthRoutine,
            'youthPositiveExperiences' : self.youthPositiveExperiences,
            'youthNegativeExperiences' : self.youthNegativeExperiences,
            'youthResponsabilities' : self.youthResponsabilities,
            'youthAddress' : self.youthAddress,
            'youthLikes' : self.youthLikes,
            'youthHobbies' : self.youthHobbies,
            'youthAfraids' : self.youthAfraids,
            'youthSentimentalCouple' : self.youthSentimentalCouple,
            'youthProjects' : self.youthProjects,
            'youthUncompletedProjects' : self.youthUncompletedProjects,
            'youthIllness' : self.youthIllness,
            'youthPersonalCrisis' : self.youthPersonalCrisis,
            'youthMusic' : self.youthMusic
        }
     
class Adulthood():
     def __init__(self, id : int, idLifeStory : int,
                  adulthoodSentimentalCouple : str, adulthoodChildren : str, adulthoodStudies : str, adulthoodWorkPlace : str,
                  adulthoodWorkRol : str, adulthoodFamilyCore : str, adulthoodFriendsGroup : str, adulthoodWorkGroup : str, adulthoodImportantPerson: str,
                  adulthoodTravels : str, adulthoodFavouritePlace : str, adulthoodRoutine : str, adulthoodPositiveExperiences : str, 
                  adulthoodNegativeExperiences : str, adulthoodResponsabilities: str, adulthoodAddress : str, adulthoodEconomicSituation : str,
                  adulthoodProjects : str, adulthoodUncompletedProjects : str, adulthoodIllness : str, adulthoodPersonalCrisis : str, adulthoodMusic : str):
          self.id = id
          self.idLifeStory = idLifeStory
          self.adulthoodSentimentalCouple = adulthoodSentimentalCouple
          self.adulthoodChildren = adulthoodChildren
          self.adulthoodStudies = adulthoodStudies
          self.adulthoodWorkPlace = adulthoodWorkPlace
          self.adulthoodWorkRol = adulthoodWorkRol
          self.adulthoodFamilyCore = adulthoodFamilyCore
          self.adulthoodFriendsGroup = adulthoodFriendsGroup
          self.adulthoodWorkGroup = adulthoodWorkGroup
          self.adulthoodImportantPerson = adulthoodImportantPerson
          self.adulthoodTravels = adulthoodTravels
          self.adulthoodFavouritePlace = adulthoodFavouritePlace
          self.adulthoodRoutine = adulthoodRoutine
          self.adulthoodPositiveExperiences = adulthoodPositiveExperiences
          self.adulthoodNegativeExperiences = adulthoodNegativeExperiences
          self.adulthoodResponsabilities = adulthoodResponsabilities
          self.adulthoodAddress = adulthoodAddress
          self.adulthoodEconomicSituation = adulthoodEconomicSituation
          self.adulthoodProjects = adulthoodProjects
          self.adulthoodUncompletedProjects = adulthoodUncompletedProjects
          self.adulthoodIllness = adulthoodIllness
          self.adulthoodPersonalCrisis = adulthoodPersonalCrisis
          self.adulthoodMusic = adulthoodMusic
     def to_dict(self): 
        return {
            'id' : self.id,
            'idLifeStory' : self.idLifeStory,
            'adulthoodSentimentalCouple' : self.adulthoodSentimentalCouple,
            'adulthoodChildren' : self.adulthoodChildren,
            'adulthoodStudies' : self.adulthoodStudies,
            'adulthoodWorkPlace' : self.adulthoodWorkPlace,
            'adulthoodWorkRol' : self.adulthoodWorkRol,
            'adulthoodFamilyCore' : self.adulthoodFamilyCore,
            'adulthoodFriendsGroup' : self.adulthoodFriendsGroup,
            'adulthoodWorkGroup' : self.adulthoodWorkGroup,
            'adulthoodImportantPerson' : self.adulthoodImportantPerson,
            'adulthoodTravels' : self.adulthoodTravels,
            'adulthoodFavouritePlace' : self.adulthoodFavouritePlace,
            'adulthoodRoutine' : self.adulthoodRoutine,
            'adulthoodPositiveExperiences' : self.adulthoodPositiveExperiences,
            'adulthoodNegativeExperiences' : self.adulthoodNegativeExperiences,
            'adulthoodResponsabilities' : self.adulthoodResponsabilities,
            'adulthoodAddress' : self.adulthoodAddress,
            'adulthoodEconomicSituation' : self.adulthoodEconomicSituation,
            'adulthoodProjects' : self.adulthoodProjects,
            'adulthoodUncompletedProjects' : self.adulthoodUncompletedProjects,
            'adulthoodIllness' : self.adulthoodIllness,
            'adulthoodPersonalCrisis' : self.adulthoodPersonalCrisis,
            'adulthoodMusic' : self.adulthoodMusic
        }
     
class Maturity():
     def __init__(self, id : int, idLifeStory : int,
                  maturityGrandchildren : str, maturityWorkPlace : str, maturityWorkRol : str, maturityFamilyCore : str,
                  maturityFriendsGroup : str, maturityWorkGroup : str, maturityImportantPerson: str, maturityTravels : str, maturityFavouritePlace : str,
                  maturityRoutine : str, maturityPositiveExperiences : str, maturityNegativeExperiences : str,maturityResponsabilities: str, 
                  maturityRetirement : str, maturityWills : str, maturityProjects : str, maturityUncompletedProjects : str,
                  maturityIllness : str, maturityPersonalCrisis : str, maturityMusic : str):
          self.id = id
          self.idLifeStory = idLifeStory
          self.maturityGrandchildren = maturityGrandchildren
          self.maturityWorkPlace = maturityWorkPlace
          self.maturityWorkRol = maturityWorkRol
          self.maturityFamilyCore = maturityFamilyCore
          self.maturityFriendsGroup = maturityFriendsGroup
          self.maturityWorkGroup = maturityWorkGroup
          self.maturityImportantPerson = maturityImportantPerson
          self.maturityTravels = maturityTravels
          self.maturityFavouritePlace = maturityFavouritePlace
          self.maturityRoutine = maturityRoutine
          self.maturityPositiveExperiences = maturityPositiveExperiences
          self.maturityNegativeExperiences = maturityNegativeExperiences
          self.maturityResponsabilities = maturityResponsabilities
          self.maturityRetirement = maturityRetirement
          self.maturityWills = maturityWills
          self.maturityProjects = maturityProjects
          self.maturityUncompletedProjects = maturityUncompletedProjects
          self.maturityIllness = maturityIllness
          self.maturityPersonalCrisis = maturityPersonalCrisis
          self.maturityMusic = maturityMusic
     def to_dict(self): 
        return {
            'id' : self.id,
            'idLifeStory' : self.idLifeStory,
            'maturityGrandchildren' : self.maturityGrandchildren,
            'maturityWorkPlace' : self.maturityWorkPlace,
            'maturityWorkRol' : self.maturityWorkRol,
            'maturityFamilyCore' : self.maturityFamilyCore,
            'maturityFriendsGroup' : self.maturityFriendsGroup,
            'maturityWorkGroup' : self.maturityWorkGroup,
            'maturityImportantPerson' : self.maturityImportantPerson,
            'maturityTravels' : self.maturityTravels,
            'maturityFavouritePlace' : self.maturityFavouritePlace,
            'maturityRoutine' : self.maturityRoutine,
            'maturityPositiveExperiences' : self.maturityPositiveExperiences,
            'maturityNegativeExperiences' : self.maturityNegativeExperiences,
            'maturityResponsabilities' : self.maturityResponsabilities,
            'maturityRetirement' : self.maturityRetirement,
            'maturityWills' : self.maturityWills,
            'maturityProjects' : self.maturityProjects,
            'maturityUncompletedProjects' : self.maturityUncompletedProjects,
            'maturityIllness' : self.maturityIllness,
            'maturityPersonalCrisis' : self.maturityPersonalCrisis,
            'maturityMusic' : self.maturityMusic
        }

class Personality():
     def __init__(self, id : int, idPaciente : int,
                  nature : str, habits : str, likes : str, dislikes : str, calmMethods : str, disturbMethods : str, hobbies : str,
                  technologyLevel : str, goals : str, favouriteSongs : str, clothes: str):
          self.id = id
          self.idPaciente = idPaciente
          self.nature = nature
          self.habits = habits
          self.likes = likes
          self.dislikes = dislikes
          self.calmMethods = calmMethods
          self.disturbMethods = disturbMethods
          self.hobbies = hobbies
          self.technologyLevel = technologyLevel
          self.goals = goals
          self.favouriteSongs = favouriteSongs
          self.clothes = clothes
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
          'hobbies' : self.hobbies,
          'technologyLevel' : self.technologyLevel,
          'goals' : self.goals,
          'favouriteSongs' : self.favouriteSongs,
          'clothes' : self.clothes
        }
     
class ContactData():
     def __init__(self, id : int, idPaciente : int,
                  contactName : str, contactFirstName : str, contactSecondSurname : str, contactAddress : str, contactEmail : str, contactTelecom : str,contactTelegram : str, curatela : str, deFactoGuardian : str):
          self.id = id
          self.idPaciente = idPaciente
          self.contactName = contactName
          self.contactFirstSurname = contactFirstName
          self.contactSecondSurname = contactSecondSurname
          self.contactAddress = contactAddress
          self.contactEmail = contactEmail
          self.contactTelecom = contactTelecom
          self.contactTelegram = contactTelegram
          self.curatela = curatela
          self.deFactoGuardian = deFactoGuardian
     def to_dict(self): 
        return {
            'id' : self.id,
            'idPaciente' : self.idPaciente,
            'contactName' : self.contactName,
            'contactFirstSurname' : self.contactFirstSurname,
            'contactSecondSurname' : self.contactSecondSurname,
            'contactAddress' : self.contactAddress,
            'contactEmail' : self.contactEmail,
            'contactTelecom' : self.contactTelecom,
            'contactTelegram' : self.contactTelegram,
            'curatela' : self.curatela,
            'deFactoGuardian' : self.deFactoGuardian
        }
     
class MainSanitaryData():
     def __init__(self, id : int, idPaciente : int, 
                  mainIllness : str, allergies : str, otherIllness : str):
          self.id = id
          self.idPaciente = idPaciente
          self.mainIllness = mainIllness
          self.allergies = allergies
          self.otherIllness = otherIllness
     def to_dict(self): 
        return {
            'id' : self.id,
            'idPaciente' : self.idPaciente,
            'mainIllness' : self.mainIllness,
            'allergies' : self.allergies,
            'otherIllness' : self.otherIllness
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
                  nutritionalSituation : str, sleepQuality : str, fallRisks : str, mobilityNeeds : str, healthPreferences : str):
          self.id = id
          self.idSanitary = idSanitary
          self.nutritionalSituation = nutritionalSituation
          self.sleepQuality = sleepQuality
          self.fallRisks = fallRisks
          self.mobilityNeeds = mobilityNeeds
          self.healthPreferences = healthPreferences
     def to_dict(self): 
        return {
            'id' : self.id,
            'idSanitary' : self.idSanitary,
            'nutritionalSituation' : self.nutritionalSituation,
            'sleepQuality' : self.sleepQuality,
            'fallRisks' : self.fallRisks,
            'mobilityNeeds' : self.mobilityNeeds,
            'healthPreferences' : self.healthPreferences
        }
     
class SocialEducationOccupationalTherapy():
     def __init__(self, id : int, idSanitary: int,
                  cognitiveAbilities : str, affectiveCapacity : str, behaviorCapacity : str, collaborationLevel : str, autonomyLevel : str, groupParticipation : str,):
          self.id = id
          self.idSanitary = idSanitary
          self.cognitiveAbilities = cognitiveAbilities
          self.affectiveCapacity = affectiveCapacity
          self.behaviorCapacity = behaviorCapacity
          self.collaborationLevel = collaborationLevel
          self.autonomyLevel = autonomyLevel
          self.groupParticipation = groupParticipation
     def to_dict(self): 
        return {
            'id' : self.id,
            'idSanitary' : self.idSanitary,
            'cognitiveAbilities' : self.cognitiveAbilities,
            'affectiveCapacity' : self.affectiveCapacity,
            'behaviorCapacity' : self.behaviorCapacity,
            'collaborationLevel' : self.collaborationLevel,
            'autonomyLevel' : self.autonomyLevel,
            'groupParticipation' : self.groupParticipation
        }

class SocialWork():
     def __init__(self, id : int, idSanitary: int,
                  residentAndRelationship : str, petNameAndBreedPet : str, resources : str, legalSupport : str):
          self.id = id
          self.idSanitary = idSanitary
          self.residentAndRelationship = residentAndRelationship
          self.petNameAndBreedPet = petNameAndBreedPet
          self.resources = resources
          self.legalSupport = legalSupport
     def to_dict(self): 
        return {
            'id' : self.id,
            'idSanitary' : self.idSanitary,
            'residentAndRelationship' : self.residentAndRelationship,
            'petNameAndBreedPet' : self.petNameAndBreedPet,
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
                  photoReferences : str, photoCategory):
          self.id = id
          self.idPaciente = idPaciente
          self.photoReferences = photoReferences
          self.photoCategory = photoCategory

     def to_dict(self): 
        return {
            'id' : self.id,
            'idPaciente' : self.idPaciente,
            'photoReferences' : self.photoReferences,
            'photoCategory' : self.photoCategory
        }