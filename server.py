from flask import Flask, request, jsonify
from flask_cors import CORS
from flaskext.mysql import MySQL
from flask_mail import Mail, Message
from dotenv import load_dotenv
import logging
from flask_jwt_extended import jwt_required, JWTManager, create_access_token
import os
import jwt
from datetime import timedelta

from models.ModelUser import ModelUser
from models.ModelRoles import ModelRoles
from models.ModelOrganizacion import ModelOrganizacion
from models.ModelPaciente import ModelPaciente


app = Flask(__name__)

# Cargar variables de entorno
load_dotenv()

# Variables globales
FRONTEND_API_URL = os.getenv('FRONTEND_API_URL')
MAIL_SENDER = os.getenv('MAIL_SENDER')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

# Configuración de la base de datos MySQL
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DB_HOST')
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DB_NAME')

# Configuración de la conexión al servidor de mail
app.config['MAIL_SERVER']= os.getenv('MAIL_HOST')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] =  os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Configuración de CORS
CORS(app)

#Configuración de JWT
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)

#Configuración de Logger
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s',
)
logger = logging.getLogger("LoginModule")

# Inicializar MySQL
mysql = MySQL()
mysql.init_app(app)


    # ------------------- LOG IN -------------------  #
@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    try:
        usuario = ModelUser.login(mysql,email,password)
        if isinstance(usuario, dict):
            token = create_access_token(identity=usuario['id'])
            return jsonify({'message': 'Login exitoso', 'usuario': usuario, 'token':token}), 200
    except Exception as e:
        return jsonify({'error': 'Email o contraseña incorrectos'}), 401

    # ------------------- USUARIOS ------------------- #

@app.route('/crearUsuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    password = data.get('password')
    organizacion = data.get('organizacion')
    rol = data.get('rol')   
    
    try:        
        usuario = ModelUser.createUser(mysql, nombre, email, password, organizacion['id'], rol)
        return jsonify({'message':'Usuario creado correctamente.', 'usuario':usuario}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido crear el usuario.'}), 400

@app.route('/getUsuarios', methods=['GET'])
@jwt_required()
def get_usuarios():
    organizacion = request.args.get('org')
    
    try:
        usuarios = ModelUser.getAllUsers(mysql, organizacion)
        return jsonify({'message': 'Usuarios obtenidos', 'usuarios':usuarios}), 200
    except Exception as e:
        return jsonify({'message': 'No se ha podido obtener los usuarios'}), 400

@app.route('/getUsuario', methods=['GET'])
@jwt_required()
def get_usuario():
    usuarioId = request.args.get('id')
    
    try:
        usuario = ModelUser.getUsuario(mysql, usuarioId)
        
        return jsonify({'message': 'Usuario obtenidos', 'usuario':usuario}), 200
    except Exception as e:
        return jsonify({'message': 'No se ha podido obtener el usuario'}), 400

@app.route('/eliminarUsuario', methods=['POST'])
@jwt_required()
def eliminar_usuario():
    data = request.get_json()
    usuarioId = data.get('usuarioId')
    
    try:
        
        ModelUser.deleteUser(mysql, usuarioId)
        
        return jsonify({'message': 'Usuario eliminado'}), 200
    except Exception as e:
        return jsonify({'message': 'No se ha podido eliminar el usuario'}), 400
    
    
@app.route('/modificarUsuario', methods=['PUT'])
@jwt_required()
def modificar_usuario():
    data = request.get_json()
    usuario = data.get('mostrarUsuario')
    usuarioId = usuario['id']
    nombre = usuario['name']
    email = usuario['email']
    idOrganizacion = usuario['idOrganizacion']
    roles = usuario['roles']
    
    try:
        usuario = ModelUser.updateDataUser(mysql, usuarioId, nombre, email, idOrganizacion, roles)
        
        return jsonify({'message': 'Usuario modificado correctamente', 'usuario':usuario}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido modificar el usuario'}), 400
    
@app.route('/modificarPassword', methods=['PUT'])
@jwt_required()
def modificar_password():
    data = request.get_json()
    usuarioId = data.get('id')
    newPassword = data.get('newPassword')
    password = newPassword['nuevaContraseña']
    
    try:        
        ModelUser.updatePassword(mysql, usuarioId, password)
        return jsonify({'message': 'Contraseña modificada correctamente.'}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido modificar la contraseña.'}), 400
    
@app.route('/recuperarPassword', methods=['POST'])
def recuperar_password():
    data = request.get_json()
    email = data.get('email')
    password = data.get('newPassword')
    try:
        usuarioId = ModelUser.getUserByEmail(mysql, email)
        if not usuarioId:
            return jsonify({'error': 'No se ha encontrado el usuario'}), 404
        
        ModelUser.updatePassword(mysql, usuarioId, password)
        return jsonify({'message': 'Contraseña recuperada correctamente.'}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido recuperar la contraseña.'}), 400
    
    # ------------------- PACIENTES ------------------- #
    
@app.route('/getPacientes', methods=['GET'])
@jwt_required()
def get_pacientes():
    idOrganizacion = request.args.get('idOrganizacion')
    
    try:
        pacientes = ModelPaciente.getPacientes(mysql, idOrganizacion)
        if not pacientes:
            return jsonify({'error': 'No se han encontrado pacientes'}), 404
        return jsonify({'message': 'Pacientes obtenidos', 'pacientes':pacientes}), 200
    except:
        return jsonify({'error':'Error al obtener los pacientes.'}), 400

@app.route('/getPaciente', methods=['GET'])
@jwt_required()
def get_paciente():
    pacienteId = request.args.get('id')
    
    try:
        paciente = ModelPaciente.getPaciente(mysql, pacienteId)
        
        return jsonify({'message': 'Usuario obtenidos', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error': 'Usuario no encontrado'})

@app.route('/crearPaciente', methods=['POST'])
@jwt_required()
def crear_paciente():
    data = request.get_json()
    name = data.get('nombre')
    firstSurname = data.get('primerApellido')
    secondSurname = data.get('segundoApellido')
    alias = data.get('alias')
    birthDate = data.get('fechaNacimiento')
    age = data.get('edad')
    birthPlace = data.get('lugarNacimiento')
    address = data.get('direccion')
    nationality = data.get('nacionalidad')
    gender = data.get('genero')
    maritalStatus = data.get('estadoCivil')
    language = data.get('idioma')
    otherLanguages = data.get('otrosIdiomas')
    culturalHeritage = data.get('origenCultural')
    faith = data.get('creencias')
    imgPerfil = data.get('imgPerfil')
    idOrganizacion = data.get('idOrganizacion')
    
    try:
        pacienteId = ModelPaciente.createPaciente(mysql,idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,
                       nationality,gender,address,maritalStatus,language,otherLanguages,culturalHeritage,faith)
        return jsonify({'message': 'Paciente creado correctamente.', 'paciente':pacienteId}), 200
    except Exception as e:
        return jsonify({'error':'Error al añadir el paciente.'}), 400

@app.route('/eliminarPaciente', methods=['POST'])
@jwt_required()
def eliminar_pacientes():
    data = request.get_json()
    pacienteId = data.get('pacienteId')
    
    ModelPaciente.deletePaciente(mysql, pacienteId)  
        
    return jsonify({'message':'Paciente eliminado correctamente.'}), 200


    # ------------------- PACIENTES | PERSONALIDAD ------------------- #
    
@app.route('/pacientePersonality', methods=['GET'])
@jwt_required()
def get_paciente_personality():
    pacienteId = request.args.get('id')
    
    try:
        pacientePersonality = ModelPaciente.getPersonalityPaciente(mysql, pacienteId)
        if not pacientePersonality:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos personales obtenidos', 'personality':pacientePersonality}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos personales.'}), 400
    
    
@app.route('/pacientePersonality', methods=['POST'])
@jwt_required()
def post_paciente_personality():
    data = request.get_json()
    pacienteId = data.get('id')
    nature = data.get('nature')
    habits = data.get('habits')
    likes = data.get('likes')
    dislikes = data.get('dislikes')
    calmMethods = data.get('calmMethods')
    disturbMethods = data.get('disturbMethods')
    hobbies = data.get('hobbies')
    technologyLevel = data.get('technologyLevel')
    goals = data.get('goals')
    
    try:
        paciente = ModelPaciente.createPersonalityPaciente(mysql, pacienteId, nature, habits, likes, dislikes, calmMethods,disturbMethods,hobbies,technologyLevel,goals)
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos personales obtenidos', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos personales.'}), 400
    
    # ------------------- PACIENTES | DATOS DE CONTACTO ------------------- #
    
@app.route('/pacienteDatosContacto', methods=['GET'])
def get_paciente_datoscontacto():
    pacienteId = request.args.get('id')
    
    try:
        pacienteDatosContacto = ModelPaciente.getContactDataPaciente(mysql, pacienteId)
        if not pacienteDatosContacto:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos de contacto obtenidos', 'contactdata':pacienteDatosContacto}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos de contacto.'}), 400
    
@app.route('/pacienteDatosContacto', methods=['POST'])
def post_paciente_datoscontacto():
    data = request.get_json()
    pacienteId = data.get('id')
    contactdata = data.get('contactdata')
    
    try:
        paciente = ModelPaciente.createContactDataPaciente(mysql, pacienteId, contactdata["contactName"], contactdata['contactFirstSurname'], contactdata['contactSecondSurname'], contactdata['contactAddress'], contactdata['contactEmail'], contactdata['contactTelecom'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos de contacto obtenidos', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos de contacto.'}), 400

    # ------------------- PACIENTES | INFANCIA ------------------- #
    
@app.route('/pacienteInfancia', methods=['GET'])
def get_paciente_infancia():
    pacienteId = request.args.get('id')
    
    try:
        pacienteInfancia = ModelPaciente.getChildhoodPaciente(mysql, pacienteId)
        if not pacienteInfancia:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos de infancia obtenidos', 'infancia':pacienteInfancia}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos de infancia.'}), 400
    
@app.route('/pacienteInfancia', methods=['POST'])
def post_paciente_infancia():
    data = request.get_json()
    pacienteId = data.get('id')
    childhood = data.get('childhood')
    
    try:
        paciente = ModelPaciente.createChildhoodPaciente(mysql, pacienteId, childhood["childhoodStudies"], childhood['childhoodSchool'], childhood['childhoodMotivations'], childhood['childhoodFamilyCore'], childhood['childhoodFriendsGroup'], childhood['childhoodTravels'], childhood['childhoodFavouritePlace'], childhood["childhoodPositiveExperiences"], childhood['childhoodNegativeExperiences'], childhood['childhoodAddress'], childhood['childhoodLikes'], childhood['childhoodAfraids'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos de infancia obtenidos', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos de infancia.'}), 400

    # ------------------- PACIENTES | JUVENTUD ------------------- #
    
@app.route('/pacienteJuventud', methods=['GET'])
def get_paciente_juventud():
    pacienteId = request.args.get('id')
    
    try:
        pacienteJuventud = ModelPaciente.getYouthPaciente(mysql, pacienteId)
        if not pacienteJuventud:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos de juventud obtenidos', 'juventud':pacienteJuventud}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos de juventud.'}), 400
    
@app.route('/pacienteJuventud', methods=['POST'])
def post_paciente_juventud():
    data = request.get_json()
    pacienteId = data.get('id')
    youth = data.get('youth')
    

    try:
        paciente = ModelPaciente.createYouthPaciente(mysql, pacienteId, youth["youthStudies"], youth['youthSchool'], youth['youthWorkPlace'], youth['youthWorkRol'], youth['youthFamilyCore'], youth['youthFriendsGroup'], youth['youthTravels'], youth['youthFavouritePlace'], youth['youthRoutine'], youth['youthPositiveExperiences'], youth['youthNegativeExperiences'], youth['youthAddress'], youth['youthLikes'], youth['youthHobbies'], youth['youthAfraids'], youth['youthProjects'], youth['youthUncompletedProjects'], youth['youthIllness'], youth['youthPersonalCrisis'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos de juventud obtenidos', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos de juventud.'}), 400
        
    # ------------------- PACIENTES | ADULTEZ ------------------- #
    
@app.route('/pacienteAdultez', methods=['GET'])
def get_paciente_adultez():
    pacienteId = request.args.get('id')
    
    try:
        pacienteAdultez = ModelPaciente.getAdulthoodPaciente(mysql, pacienteId)
        if not pacienteAdultez:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos de adultez obtenidos', 'adultez':pacienteAdultez}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos de adultez.'}), 400
    
@app.route('/pacienteAdultez', methods=['POST'])
def post_paciente_adultez():
    data = request.get_json()
    pacienteId = data.get('id')
    adulthood = data.get('adulthood')

    try:
        paciente = ModelPaciente.createAdulthoodPaciente(mysql, pacienteId, adulthood["adulthoodSentimentalCouple"], adulthood['adulthoodChildren'], adulthood['adulthoodStudies'], adulthood['adulthoodWorkPlace'], adulthood['adulthoodWorkRol'], adulthood['adulthoodFamilyCore'], adulthood['adulthoodFriendsGroup'], adulthood['adulthoodWorkGroup'], adulthood['adulthoodTravels'], adulthood['adulthoodFavouritePlace'], adulthood['adulthoodRoutine'], adulthood['adulthoodPositiveExperiences'], adulthood['adulthoodNegativeExperiences'], adulthood['adulthoodAddress'], adulthood['adulthoodEconomicSituation'], adulthood['adulthoodProjects'], adulthood['adulthoodUncompletedProjects'], adulthood['adulthoodIllness'], adulthood['adulthoodPersonalCrisis'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos de adultez obtenidos', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos de adultez.'}), 400
    
    # ------------------- PACIENTES | MADUREZ ------------------- #
    
@app.route('/pacienteMadurez', methods=['GET'])
def get_paciente_madurez():
    pacienteId = request.args.get('id')
    
    try:
        pacienteMadurez = ModelPaciente.getMaturityPaciente(mysql, pacienteId)
        if not pacienteMadurez:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos de madurez obtenidos', 'madurez':pacienteMadurez}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos de madurez.'}), 400
    
@app.route('/pacienteMadurez', methods=['POST'])
def post_paciente_madurez():
    data = request.get_json()
    pacienteId = data.get('id')
    maturity = data.get('maturity')

    try:
        paciente = ModelPaciente.createMaturityPaciente(mysql, pacienteId, maturity['maturityGrandchildren'], maturity['maturityWorkPlace'], maturity['maturityWorkRol'], maturity['maturityFamilyCore'], maturity['maturityFriendsGroup'], maturity['maturityWorkGroup'], maturity['maturityTravels'], maturity['maturityFavouritePlace'], maturity['maturityRoutine'], maturity['maturityPositiveExperiences'], maturity['maturityNegativeExperiences'], maturity['maturityRetirement'], maturity['maturityWills'], maturity['maturityProjects'], maturity['maturityUncompletedProjects'], maturity['maturityIllness'], maturity['maturityPersonalCrisis'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Datos de madurez obtenidos', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los datos de madurez.'}), 400
    
    # ------------------- PERSONAS DE REFERENCIA | FAMILIARES ------------------- #
    
@app.route('/getPacientesReferencia', methods=['GET'])
def get_pacientes_referencia():
    user = request.args.get('user')
    
    try:
        pacientes = ModelPaciente.getPacientesReferencia(mysql, user)
        if not pacientes:
            return jsonify({'message': 'No tiene asignado a ningún paciente'}), 200
        return jsonify({'message': 'Pacientes obtenidos', 'pacientes':pacientes}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los pacientes.'}), 400
    
@app.route('/getUsuariosReferencia', methods=['GET'])
@jwt_required()
def get_usuarios_referencia():
    pacienteId = request.args.get('id')
    try:
        usuarios = ModelUser.getPersonalReferencia(mysql, pacienteId)
        if not usuarios:
            return jsonify({'message': 'No tiene asignado a ningún usuario'}), 200
        return jsonify({'message': 'Pacientes obtenidos', 'usuarios':usuarios}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los pacientes.'}), 400
    
@app.route('/asignarPersonaReferencia', methods=['POST'])
@jwt_required()
def asignar_persona_referencia():
    data = request.get_json()
    pacienteId = data.get('pacienteId')
    usuarioId = data.get('usuarioId')
    
    try:
        ModelPaciente.asignarPersonaReferencia(mysql, pacienteId, usuarioId)
        return jsonify({'message': 'Persona de referencia asignada correctamente'}), 200
    except Exception as e:
        return jsonify({'error':'Error al asignar la persona de referencia.'}), 400
    
    # ------------------- ORGANIZACIONES ------------------- #
    
@app.route('/getOrganizacion', methods=['GET'])
@jwt_required()
def get_organizacion():
    organizacionId = request.args.get('org')
    
    try:
        organizacion = ModelOrganizacion.getOrganizacion(mysql, organizacionId)
        
        return jsonify({'message': 'Organizacion obtenida', 'organizacion':organizacion}), 200
    
    except Exception as e:
        return jsonify({'error': 'error'}), 401
    
    
    # ------------------- ROLES ------------------- #

@app.route('/getRoles', methods=['GET'])
@jwt_required()
def get_roles():
    
    try:
        roles = ModelRoles.getAllRoles(mysql)
        if roles:
            return jsonify({'message':'ok', 'roles':roles}), 200
        else:
            return jsonify({'error': 'error'}), 401
    except Exception as e:
        return jsonify({'error':'error'}), 400
    
    
    # ------------------- IMAGENES ------------------- #
    
@app.route('/getImagenesPaciente', methods=['GET'])
@jwt_required()
def get_imagenes_paciente():
    return jsonify({'message': 'Imagenes obtenidas'}), 200
    
     # ------------------- EMAILS ------------------- #
     
@app.route('/sendMailInvitacion', methods=['POST'])
@jwt_required()
def sendMailInvitacion():
    data = request.get_json()
    email = data.get('email')
    organizacion = data.get('organizacion')
    rol = data.get('rol')
    
    try:
        msg = Message(
            'Invitación a Cuidatiavita',
            recipients=[email],
            sender=('Cuidatia Vita', MAIL_SENDER),
        )
        
        msg.html = f"""
            <p>Hola,</p>
            <p>Únete a Cuidatia Vita. Haga click en el siguiente enlace para aceptar la invitación:</p>
            <a href="{FRONTEND_API_URL}personal/create?m={email}&r={rol}&o={organizacion}">Aceptar invitación</a>
        """
        
        mail.send(msg)
        return jsonify({'message': 'Email enviado correctamente'}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido enviar el email'}), 400
    
@app.route('/sendMailRecuperacion', methods=['POST'])
def sendMailRecuperar():
    data = request.get_json()
    email = data.get('email')
    
    try:
        msg = Message(
            'Recuperación de contraseña',
            recipients=[email],
            sender=('Cuidatia Vita', MAIL_SENDER),
        ) 
        
        msg.html = f"""
            <p>Hola,</p>
            <p>Ha solcitado la recuperación de contraseña, pulse en el siguiente enlace para proceder:</p>
            <a href="{FRONTEND_API_URL}recuperacion-contrasena/recuperar?m={email}">Click aquí</a>
        """
        
        mail.send(msg) 
        return jsonify({'message': 'Email enviado correctamente'}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido enviar el email'}), 400



if __name__ == "__main__":
    app.run(debug=True)