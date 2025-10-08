from flask import Flask, request, jsonify, render_template, make_response
import pdfkit
from flask_cors import CORS
from flaskext.mysql import MySQL
from flask_mail import Mail, Message
from dotenv import load_dotenv
import logging
from flask_jwt_extended import jwt_required, JWTManager, create_access_token, get_jwt_identity
import os
import jwt as pyjwt
import locale
from datetime import timedelta, date, datetime
import tempfile
import smtplib
from email.mime.text import MIMEText
import requests
import boto3
from werkzeug.utils import secure_filename
import uuid
import ssl
from email.message import EmailMessage
import mysql.connector
import time

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

#Para videollamadas
APP_ID = "76229e5034a44a578d16284182629bc5"
APP_CERTIFICATE = "849350830aed4637996f482fdbf300ca"

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

# Configuración de imágenes Amazon S3
S3_BUCKET = "historiavidacuidatia"
S3_REGION = "eu-west-1"
s3 = boto3.client(
    "s3",
    aws_access_key_id="AKIAWEM74DY7VI672DOQ",
    aws_secret_access_key="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",
    region_name="eu-west-1"
)

# Configuración de la conexión a Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

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

ENTIDADES_EXTERNAS = {
    "entidad_publica_salud": "claveSuperSecreta123"
}


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
        usuario = ModelUser.createUser(mysql, nombre, email, password, organizacion, rol)
        return jsonify({'message':'Usuario creado correctamente.', 'usuario':usuario}), 200
    except Exception as e:
        print("Error en crear_usuario:", e)
        return jsonify({'error': 'No se ha podido crear el usuario.'}), 400

@app.route('/getAllUsuarios', methods=['GET'])
@jwt_required()
def get_all_usuarios():

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit
    
    try:

        total = len(ModelUser.getAllUsuarios(mysql))
        usuarios = ModelUser.getAllUsuariosPagina(mysql, limit, offset)
        return jsonify({'message': 'Usuarios obtenidos', 'usuarios':usuarios, 'totalUsuarios':total}), 200
    except Exception as e:
        return jsonify({'message': 'No se ha podido obtener los usuarios'}), 400

@app.route('/getUsuarios', methods=['GET'])
@jwt_required()
def get_usuarios():
    organizacion = request.args.get('org')

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit
    
    try:

        total = len(ModelUser.getAllUsers(mysql, organizacion))
        usuarios = ModelUser.getUsuariosPagina(mysql, organizacion, limit, offset)
        return jsonify({'message': 'Usuarios obtenidos', 'usuarios':usuarios, 'totalUsuarios':total}), 200
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
    
@app.route('/searchUsuario', methods=['GET'])
@jwt_required()
def buscar_usuarios():
    nombre = request.args.get('nombre', '').lower()
    idOrganizacion = request.args.get('idOrganizacion')

    try:
        if idOrganizacion is None:
            usuarios = ModelUser.getAllUsuarios(mysql)
        else:
            usuarios = ModelUser.getAllUsers(mysql, idOrganizacion)
        usuarios_filtrados = [
            usuario for usuario in usuarios
            if nombre in usuario['nombre'].lower()
        ]
        return jsonify({'message': 'Usuarios filtrados', 'usuarios': usuarios_filtrados}), 200
    except Exception as e:
        return jsonify({'error': 'Error al buscar usuarios'}), 400

@app.route('/getPersonalName', methods=['GET'])
@jwt_required()
def get_personal_name():
    usuarioId = request.args.get('id') 
    try:
        usuario = ModelUser.getUsuario(mysql, usuarioId)
        personalNombreCompleto = usuario['nombre']
        if personalNombreCompleto:
            return jsonify({'message': 'Usuario obtenido', 'personalNombreCompleto': personalNombreCompleto}), 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': 'Error al obtener el paciente'}), 500

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
    nombre = usuario['nombre']
    email = usuario['email']
    idOrganizacion = usuario['idOrganizacion']
    roles = usuario['roles']
    idTelegram = usuario['idTelegram']
    
    try:
        usuario = ModelUser.updateDataUser(mysql, usuarioId, nombre, email, idOrganizacion, roles, idTelegram)
        
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
@app.route('/getAllPacientes', methods=['GET'])
@jwt_required()
def get_all_pacientes():

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit

    try:
        total = len(ModelPaciente.getAllPacientes(mysql))
        pacientes = ModelPaciente.getAllPacientesPagina(mysql, limit, offset)
        if not pacientes:
            return jsonify({'error': 'No se han encontrado pacientes'}), 404
        return jsonify({'message': 'Pacientes obtenidos', 'pacientes':pacientes, 'totalPacientes':total}), 200
    except Exception as e:
        return jsonify({'error':'Error al obtener los pacientes.'}), 400


@app.route('/getPacientes', methods=['GET'])
@jwt_required()
def get_pacientes():
    idOrganizacion = request.args.get('idOrganizacion')

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit

    try:
        total = len(ModelPaciente.getPacientes(mysql, idOrganizacion))
        pacientes = ModelPaciente.getPacientesPagina(mysql, idOrganizacion, limit, offset)
        if not pacientes:
            return jsonify({'error': 'No se han encontrado pacientes'}), 404
        return jsonify({'message': 'Pacientes obtenidos', 'pacientes':pacientes, 'totalPacientes':total}), 200
    except Exception as e:
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
    
@app.route('/getPacienteName', methods=['GET'])
@jwt_required()
def get_paciente_name():
    pacienteId = request.args.get('id') 
    
    try:
        paciente = ModelPaciente.getPaciente(mysql, pacienteId)
        pacienteNombreCompleto = paciente['name'] + ' ' + paciente['firstSurname'] + ' ' + paciente['secondSurname']
        
        if pacienteNombreCompleto:
            return jsonify({'message': 'Usuario obtenido', 'pacienteNombreCompleto': pacienteNombreCompleto}), 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': 'Error al obtener el paciente'}), 500
    
@app.route('/searchPaciente', methods=['GET'])
@jwt_required()
def buscar_pacientes():
    nombre = request.args.get('nombre', '').lower()
    idOrganizacion = request.args.get('idOrganizacion')

    try:
        if idOrganizacion is None:
            pacientes = ModelPaciente.getAllPacientes(mysql)
        else:
            pacientes = ModelPaciente.getPacientes(mysql, idOrganizacion)
        pacientes_filtrados = [
            paciente for paciente in pacientes
            if nombre in paciente['name'].lower()
        ]
        return jsonify({'message': 'Pacientes filtrados', 'pacientes': pacientes_filtrados}), 200
    except Exception as e:
        return jsonify({'error': 'Error al buscar pacientes'}), 400
    
@app.route('/upsertPaciente', methods=['POST'])
@jwt_required()
def upsert_paciente():
    data = request.get_json()
    name = data.get('name')
    firstSurname = data.get('firstSurname')
    secondSurname = data.get('secondSurname')
    alias = data.get('alias')
    birthDate = data.get('birthDate')
    age = data.get('age')
    birthPlace = data.get('birthPlace')
    address = data.get('address')
    nationality = data.get('nationality')
    gender = data.get('gender')
    maritalStatus = data.get('maritalStatus')
    sentimentalCouple = data.get('sentimentalCouple')
    language = data.get('language')
    otherLanguages = data.get('otherLanguages')
    culturalHeritage = data.get('culturalHeritage')
    faith = data.get('faith')
    dataTelegram = data.get('dataTelegram')
    imgPerfil = data.get('imgPerfil')
    idOrganizacion = data.get('idOrganizacion')
    paciente_id= data.get('id')
    
    try:
        pacienteUpsert = ModelPaciente.upsertPaciente(mysql,idOrganizacion,name,firstSurname,secondSurname,alias,birthDate,age,birthPlace,
                       nationality,gender,address,maritalStatus,sentimentalCouple,language,otherLanguages,culturalHeritage,faith, dataTelegram, paciente_id)
    
        return jsonify({'message': 'Paciente actualizado correctamente.', 'ok': 'ok'}), 200
    except Exception as e:
        return jsonify({'error':e}), 400
    

@app.route('/crearPaciente', methods=['POST'])
@jwt_required()
def crear_paciente():
    data = request.get_json()
    nuevoPaciente = data.get('nuevoPaciente')
    idOrganizacion = data.get('idOrganizacion')
    
    try:
        pacienteId = ModelPaciente.createPaciente(mysql,idOrganizacion,nuevoPaciente['name'],nuevoPaciente['firstSurname'],nuevoPaciente['secondSurname'],nuevoPaciente['alias'],nuevoPaciente['birthDate'],nuevoPaciente['age'],nuevoPaciente['birthPlace'],
                       nuevoPaciente['nationality'],nuevoPaciente['gender'],nuevoPaciente['address'],nuevoPaciente['maritalStatus'],nuevoPaciente['sentimentalCouple'],nuevoPaciente['language'],nuevoPaciente['otherLanguages'],nuevoPaciente['culturalHeritage'],nuevoPaciente['faith'],nuevoPaciente['dataTelegram'])
        pacienteLifeStory = ModelPaciente.createLifeStoryPaciente(mysql,pacienteId)
        mainSanitaryData = ModelPaciente.createSanitaryDataPaciente(mysql,pacienteId, None, None, None)
        return jsonify({'message': 'Paciente creado correctamente.', 'paciente':pacienteId, 'lifestory':pacienteLifeStory}), 200
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
    personality = data.get('personality')
    
    try:
        paciente = ModelPaciente.upsertPersonalityPaciente(mysql, pacienteId, personality['nature'], personality['habits'], personality['likes'], personality['dislikes'], personality['calmMethods'], personality['disturbMethods'], personality['hobbies'], personality['technologyLevel'], personality['goals'], personality['favouriteSongs'], personality['clothes'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Información guardada correctamente'}), 200
    except Exception as e:
        return jsonify({'error':'Error al guardar los datos personales.'}), 400
    
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
        paciente = ModelPaciente.upsertContactDataPaciente(mysql, pacienteId, contactdata["contactName"], contactdata['contactFirstSurname'], contactdata['contactSecondSurname'], contactdata['contactAddress'], contactdata['contactEmail'], contactdata['contactTelecom'], contactdata['contactTelegram'],contactdata['curatela'], contactdata['deFactoGuardian'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Información guardada correctamente', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al guardar los datos de contacto.'}), 400

    # ------------------- PACIENTES | INFANCIA ------------------- #
    
@app.route('/pacienteInfancia', methods=['GET'])
@jwt_required()
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
@jwt_required()
def post_paciente_infancia():
    data = request.get_json()
    pacienteId = data.get('id')
    childhood = data.get('childhood')

    try:
        paciente = ModelPaciente.upsertChildhoodPaciente(mysql, pacienteId, childhood["childhoodStudies"], childhood['childhoodSchool'], childhood['childhoodMotivations'], childhood['childhoodFamilyCore'], childhood['childhoodFriendsGroup'],childhood['childhoodImportantPerson'],childhood['childhoodTravels'], childhood['childhoodFavouritePlace'], childhood["childhoodPositiveExperiences"], childhood['childhoodNegativeExperiences'],childhood['childhoodResponsabilities'], childhood['childhoodAddress'], childhood['childhoodLikes'], childhood['childhoodAfraids'], childhood['childhoodMusic'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Información guardada correctamente', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al guardar los datos de infancia.'}), 400

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
        paciente = ModelPaciente.upsertYouthPaciente(mysql, pacienteId, youth["youthStudies"], youth['youthSchool'], youth['youthWorkPlace'], youth['youthWorkRol'], youth['youthFamilyCore'], youth['youthFriendsGroup'], youth['youthImportantPerson'],youth['youthTravels'], youth['youthFavouritePlace'], youth['youthRoutine'], youth['youthPositiveExperiences'], youth['youthNegativeExperiences'], youth['youthResponsabilities'], youth['youthAddress'], youth['youthLikes'], youth['youthHobbies'], youth['youthAfraids'],youth['youthSentimentalCouple'], youth['youthProjects'], youth['youthUncompletedProjects'], youth['youthIllness'], youth['youthPersonalCrisis'], youth['youthMusic'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Información guardada correctamente', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al guardar los datos de juventud.'}), 400
        
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
        paciente = ModelPaciente.upsertAdulthoodPaciente(mysql, pacienteId, adulthood["adulthoodSentimentalCouple"], adulthood['adulthoodChildren'], adulthood['adulthoodStudies'], adulthood['adulthoodWorkPlace'], adulthood['adulthoodWorkRol'], adulthood['adulthoodFamilyCore'], adulthood['adulthoodFriendsGroup'], adulthood['adulthoodWorkGroup'], adulthood["adulthoodImportantPerson"],adulthood['adulthoodTravels'], adulthood['adulthoodFavouritePlace'], adulthood['adulthoodRoutine'], adulthood['adulthoodPositiveExperiences'], adulthood['adulthoodNegativeExperiences'], adulthood["adulthoodResponsabilities"], adulthood['adulthoodAddress'], adulthood['adulthoodEconomicSituation'], adulthood['adulthoodProjects'], adulthood['adulthoodUncompletedProjects'], adulthood['adulthoodIllness'], adulthood['adulthoodPersonalCrisis'], adulthood['adulthoodMusic'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Información guardada correctamente', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al guardar los datos de adultez.'}), 400
    
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
        paciente = ModelPaciente.upsertMaturityPaciente(mysql, pacienteId, maturity['maturityGrandchildren'], maturity['maturityWorkPlace'], maturity['maturityWorkRol'], maturity['maturityFamilyCore'], maturity['maturityFriendsGroup'], maturity['maturityWorkGroup'], maturity['maturityImportantPerson'], maturity['maturityTravels'], maturity['maturityFavouritePlace'], maturity['maturityRoutine'], maturity['maturityPositiveExperiences'], maturity['maturityNegativeExperiences'], maturity['maturityResponsabilities'], maturity['maturityRetirement'], maturity['maturityWills'], maturity['maturityProjects'], maturity['maturityUncompletedProjects'], maturity['maturityIllness'], maturity['maturityPersonalCrisis'], maturity['maturityMusic'])
        if not paciente:
            return jsonify({'error': 'No se ha encontrado el paciente'}), 404
        return jsonify({'message': 'Información guardada correctamente', 'paciente':paciente}), 200
    except Exception as e:
        return jsonify({'error':'Error al guardar los datos de madurez.'}), 400
    
    
    # ------------------- PACIENTES | MAIN SANITARY DATA ------------------- #
    
@app.route('/pacienteMainSanitaryData', methods=['GET'])
@jwt_required()
def get_main_sanitary_data():
    idPaciente = request.args.get('id')
    try:
        mainSanitaryData = ModelPaciente.getSanitaryDataPaciente(mysql,idPaciente)
        return jsonify({'message': 'Información del paciente obtenida', 'sanitaryData': mainSanitaryData})
    except Exception as e:
        return jsonify({'error': 'No se ha podido obtener la información del usuario'})
    

@app.route('/pacienteMainSanitaryData', methods=['POST'])
@jwt_required()
def post_main_sanitary_data():
    data = request.get_json()
    idPaciente = data.get('id')
    mainSanitaryData = data.get('mainSanitaryData')
    try:
        mainSanitaryData = ModelPaciente.updateSanitaryDataPaciente(mysql,idPaciente, mainSanitaryData['mainIllness'], mainSanitaryData['allergies'], mainSanitaryData['otherIllness'])
        return jsonify({'message': 'Información guardada correctamente'})
    except Exception as e:
        return jsonify({'error': 'No se ha podido guardar la información del usuario'})

# ------------------- PACIENTES | NURSING ------------------- #

@app.route('/pacienteMedicinaEnfermeria', methods=['GET'])
@jwt_required()
def get_medicina_enfermeria():
    idPaciente = request.args.get('id')
    try:
        nursing = ModelPaciente.getNursingPaciente(mysql,idPaciente)
        return jsonify({'message': 'Información del paciente obtenida', 'nursing': nursing}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido obtener la información del usuario'}), 400


@app.route('/pacienteMedicinaEnfermeria', methods=['POST'])
@jwt_required()
def post_medicina_enfermeria():
    data = request.get_json()
    idPaciente = data.get('id')
    nursing = data.get('nursing')
    
    try:
        nursing = ModelPaciente.upsertNursingPaciente(mysql, idPaciente, nursing['nutritionalSituation'], nursing['sleepQuality'], nursing['fallRisks'], nursing['mobilityNeeds'], nursing['healthPreferences'])
        
        return jsonify({'message': 'Información guardada correctamente'}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido guardar la información del usuario'}), 400

# ------------------- PACIENTES | FARMACIA ------------------- #

@app.route('/pacienteFarmacia', methods=['GET'])
@jwt_required()
def get_farmacia():
    idPaciente = request.args.get('id')
    try:
        pharmacy = ModelPaciente.getPharmacyPaciente(mysql,idPaciente)
        return jsonify({'message': 'Información del paciente obtenida', 'pharmacy': pharmacy}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido obtener la información del usuario'}), 400


@app.route('/pacienteFarmacia', methods=['POST'])
@jwt_required()
def post_farmacia():
    data = request.get_json()
    idPaciente = data.get('id')
    pharmacy = data.get('pharmacy')
    
    try:
        pharmacy = ModelPaciente.upsertPharmacyPaciente(mysql, idPaciente, pharmacy['treatment'], pharmacy['regularPharmacy'], pharmacy['visitFrequency'], pharmacy['paymentMethod'])
        
        return jsonify({'message': 'Información guardada correctamente'}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido guardar la información del usuario'}), 400
    
# ------------------- PACIENTES | TOES ------------------- #

@app.route('/pacienteTOES', methods=['GET'])
@jwt_required()
def get_toes():
    idPaciente = request.args.get('id')
    try:
        socialedu = ModelPaciente.getSocialEdu(mysql,idPaciente)
        return jsonify({'message': 'Información del paciente obtenida', 'socialedu': socialedu}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido obtener la información del usuario'}), 400


@app.route('/pacienteTOES', methods=['POST'])
@jwt_required()
def post_toes():
    data = request.get_json()
    idPaciente = data.get('id')
    socialedu = data.get('socialedu')
    try:
        socialedu = ModelPaciente.upsertSocialEduPaciente(mysql, idPaciente, socialedu['cognitiveAbilities'], socialedu['affectiveCapacity'], socialedu['behaviorCapacity'], socialedu['collaborationLevel'], socialedu['autonomyLevel'], socialedu['groupParticipation'])
        
        return jsonify({'message': 'Información guardada correctamente'}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido guardar la información del usuario'}), 400
    
# ------------------- PACIENTES | TRABAJO SOCIAL ------------------- #

@app.route('/pacienteTrabajoSocial', methods=['GET'])
@jwt_required()
def get_trabajo_social():
    idPaciente = request.args.get('id')
    try:
        socialwork = ModelPaciente.getSocialWorkPaciente(mysql,idPaciente)
        return jsonify({'message': 'Información del paciente obtenida', 'trabajoSocial': socialwork}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido obtener la información del usuario'}), 400


@app.route('/pacienteTrabajoSocial', methods=['POST'])
@jwt_required()
def post_trabajo_social():
    data = request.get_json()
    idPaciente = data.get('id')
    socialwork = data.get('socialwork')
    
    try:
        socialwork = ModelPaciente.upsertSocialWorkPaciente(mysql, idPaciente, socialwork['residentAndRelationship'], socialwork['petNameAndBreedPet'], socialwork['resources'], socialwork['legalSupport'])
        
        return jsonify({'message': 'Información guardada correctamente'}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido guardar la información del usuario'}), 400

    
    
    # ------------------- PACIENTES | COCINA E HIGIENE ------------------- #

@app.route('/pacienteCocinaHigiene', methods=['GET'])
@jwt_required()
def get_cocina_higiene():
    idPaciente = request.args.get('id')
    try:
        kitchenHygiene = ModelPaciente.getKitchenPaciente(mysql,idPaciente)
        return jsonify({'message': 'Información del paciente obtenida', 'kitchenHygiene': kitchenHygiene})
    except Exception as e:
        return jsonify({'error': 'No se ha podido obtener la información del usuario'})


@app.route('/pacienteCocinaHigiene', methods=['POST'])
@jwt_required()
def post_cocina_higiene():
    data = request.get_json()
    idPaciente = data.get('id')
    kitchenHygiene = data.get('kitchenHygiene')
    try:
        kitchenHygiene = ModelPaciente.upsertKitchenPaciente(mysql, idPaciente, kitchenHygiene['favouriteFood'], kitchenHygiene['dietaryRestrictions'], kitchenHygiene['confortAdvices'], kitchenHygiene['routine'], kitchenHygiene['carePlan'])
        return jsonify({'message': 'Información guardada correctamente'})
    except Exception as e:
        return jsonify({'error': 'No se ha podido guardar la información del usuario'})



# ------------------- PACIENTES | OTROS ------------------- #

@app.route('/pacienteOtherData', methods=['GET'])
@jwt_required()
def get_otros():
    idPaciente = request.args.get('id')
    try:
        otherData = ModelPaciente.getOtherDataPaciente(mysql,idPaciente)
        return jsonify({'message': 'Información del paciente obtenida', 'otherData': otherData})
    except Exception as e:
        return jsonify({'error': 'No se ha podido obtener la información del usuario'})


@app.route('/pacienteOtherData', methods=['POST'])
@jwt_required()
def post_otros():
    data = request.get_json()
    idPaciente = data.get('id')
    otherData = data.get('pacienteOtros')
    try:
        otherData = ModelPaciente.upsertOtherDataPaciente(mysql, idPaciente, otherData['professionalNotes'])
        return jsonify({'message': 'Información guardada correctamente'})
    except Exception as e:
        return jsonify({'error': 'No se ha podido guardar la información del usuario'})


    # ------------------- PERSONAS DE REFERENCIA | FAMILIARES ------------------- #
    
@app.route('/getPacientesReferencia', methods=['GET'])
def get_pacientes_referencia():
    user = request.args.get('user')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit
    
    try:
        page = int(page)
        limit = int(limit)
        offset = (page - 1) * limit        

        totalPacientes = len(ModelPaciente.getPacientesReferencia(mysql, user))
        pacientes = ModelPaciente.getPacientesReferenciaPagina(mysql, user, limit, offset)
        if not pacientes:
            return jsonify({'message': 'No tiene asignado a ningún paciente'}), 404
        return jsonify({'message': 'Pacientes obtenidos', 'pacientes':pacientes, 'totalPacientes': totalPacientes}), 200
    except Exception as e:
        print("Error en get_pacientes_referencia:", e)
        return jsonify({'error': str(e)}), 400
    
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
def get_organizacion():
    organizacionId = request.args.get('org')
    
    try:
        organizacion = ModelOrganizacion.getOrganizacion(mysql, organizacionId)
        
        return jsonify({'message': 'Organizacion obtenida', 'organizacion':organizacion}), 200
    
    except Exception as e:
        print(e)
        return jsonify({'error': 'error'}), 401

@app.route('/getResumenOrganizacion', methods=['GET'])
@jwt_required()
def get_resumen_organizacion():
    organizacionId = request.args.get('org')
    is_superadmin = request.args.get('rol', 'false').lower() == 'true'

    try:
        resumen = ModelOrganizacion.getResumenOrganizacion(mysql, organizacionId, is_superadmin)
    
        return jsonify({'message': 'Resumen organizacion obtenida', 'resumen':resumen}), 200
    
    except Exception as e:
        print(e)
        return jsonify({'error': 'error'}), 401
    
@app.route('/getAllOrganizaciones', methods=['GET'])
@jwt_required()
def get_all_organizaciones():

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit
    
    try:

        total = len(ModelOrganizacion.getAllOrganizaciones(mysql))
        organizaciones = ModelOrganizacion.getAllOrganizacionesPagina(mysql, limit, offset)
        return jsonify({'message': 'Organizaciones obtenidas', 'organizaciones':organizaciones, 'totalOrganizaciones':total}), 200
    except Exception as e:
        return jsonify({'message': 'No se ha podido obtener las organizaciones'}), 400

@app.route('/crearOrganizacion', methods=['POST'])
def crear_organizacion():
    data = request.get_json().get('nuevaOrganizacion')
    nombre = data.get('nombre')
    direccion = data.get('direccion')
    localidad = data.get('localidad')
    provincia = data.get('provincia')
    codigo_postal = data.get('codigo_postal')
    telefono = data.get('telefono')
    
    try:        
        organizacion = ModelOrganizacion.createOrg(mysql, nombre, direccion, localidad, provincia, codigo_postal, telefono)
        return jsonify({'message':'Organizacion creada correctamente.', 'organizacion':organizacion}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'No se ha podido crear la organizacion.'}), 400

@app.route('/eliminarOrganizacion', methods=['POST'])
@jwt_required()
def eliminar_organizacion():
    data = request.get_json()
    organizacionId = data.get('organizacionId')
    try:
        ModelOrganizacion.deleteOrg(mysql, organizacionId)
        
        return jsonify({'message': 'Organizacion eliminada'}), 200
    except Exception as e:
        return jsonify({'message': 'No se ha podido eliminar la organizacion'}), 400
      
@app.route('/modificarOrganizacion', methods=['PUT'])
@jwt_required()
def modificar_organizacion():
    data = request.get_json()
    organizacion = data.get('mostrarOrganizacion')
    organizacionId = organizacion['id']
    nombre = organizacion['nombre']
    direccion = organizacion['direccion']
    localidad = organizacion['localidad']
    provincia = organizacion['provincia']
    codigo_postal = organizacion['codigo_postal']
    telefono = organizacion['telefono']
    
    try:
        organizacion = ModelOrganizacion.updateDataOrg(mysql, organizacionId, nombre, direccion, localidad, provincia, codigo_postal, telefono)
        
        return jsonify({'message': 'Organizacion modificada correctamente', 'organizacion':organizacion}), 200
    except Exception as e:
        return jsonify({'error': 'No se ha podido modificar la organizacion'}), 400
    
@app.route('/searchOrganizacion', methods=['GET'])
@jwt_required()
def buscar_organizaciones():
    nombre = request.args.get('nombre', '').lower()

    try:
        organizaciones = ModelOrganizacion.getAllOrganizaciones(mysql)
        organizaciones_filtradas = [
            organizacion for organizacion in organizaciones
            if nombre in organizacion['nombre'].lower()
        ]
        return jsonify({'message': 'Organizaciones filtradas', 'organizaciones': organizaciones_filtradas}), 200
    except Exception as e:
        return jsonify({'error': 'Error al buscar organizaciones'}), 400
    
@app.route('/getOrganizacionName', methods=['GET'])
@jwt_required()
def get_organizacion_name():
    organizacionId = request.args.get('id') 
    try:
        organizacion = ModelOrganizacion.getOrganizacion(mysql, organizacionId)
        organizacionNombreCompleto = organizacion['nombre']
        if organizacionNombreCompleto:
            return jsonify({'message': 'Organizacion obtenida', 'organizacionNombreCompleto': organizacionNombreCompleto}), 200
        else:
            return jsonify({'error': 'Organizacion no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': 'Error al obtener la organizacion'}), 500
    
    
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
    idPaciente = request.args.get("id")
    if not idPaciente:
        return jsonify({"error": "Falta idPaciente"}), 400

    data = ModelPaciente.getImagesPaciente(mysql, idPaciente)
    if data is None:
        return jsonify({"error": "No se pudieron obtener imágenes"}), 500

    for cat, imgs in data.items():
        for img in imgs:
            signed_url = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': S3_BUCKET, 'Key': img["src"]},
                ExpiresIn=3600
            )
            img["src"] = signed_url

    return jsonify({"imagenes": data}), 200

@app.route('/uploadImagenPaciente', methods=['POST'])
@jwt_required()
def upload_imagen_paciente():
    if 'file' not in request.files:
        return jsonify({"error": "No se envió archivo"}), 400

    file = request.files['file']
    idPaciente = request.form.get("idPaciente")
    categoria = request.form.get("categoria")

    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4().hex}_{filename}"

    try:
        s3.upload_fileobj(
            file,
            S3_BUCKET,
            unique_filename,
            ExtraArgs={"ContentType": file.content_type}
        )

        #url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{unique_filename}"

        url = ModelPaciente.createImagesPaciente(mysql, idPaciente, unique_filename, categoria)

        return jsonify({"message": "Imagen subida"}), 201
    except Exception as e:
        print("Error al subir:", e)
        return jsonify({"error": "Falló subida"}), 500
    
     # ------------------- EMAILS ------------------- #
@app.route('/sendMailInvitacion', methods=['POST'])
@jwt_required()
def sendMailInvitacion():
    data = request.get_json()
    smtp_server = "server.kinetica.es"  
    smtp_port = 587
    sender_email = "cuidatia@cuidatia.org"
    sender_password = "28uvy7!5U"
    receiver_email = data.get('email')
    organizacion = data.get('organizacion')
    roles = data.get('rol')

    subject = "Invitación a Cuidatiavita"
    body = f"""
             Buenos días,

             Únete a Cuidatia Vita. Haga click en el siguiente enlace para aceptar la invitación:

             {FRONTEND_API_URL}personal/create?m={receiver_email}&r={roles}&o={organizacion}
         """

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)

    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, sender_password)
            server.send_message(message)
            print("Correo enviado con éxito.")
            return jsonify({"message": "Correo enviado con éxito"}), 200
    except smtplib.SMTPAuthenticationError as e:
        print("Fallo de autenticación:", e.smtp_error.decode())
        return jsonify({"error": "Fallo de autenticación"}), 401
    except Exception as e:
        print("Otro error:", e)
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/decoded', methods=['POST'])
def decoded_token():
    data = request.get_json()
    token = data.get('token')
    
    try:
        decoded = pyjwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        return jsonify({
            'decoded': decoded
        })
    except pyjwt.ExpiredSignatureError:
        return jsonify({'error': 'El enlace ha expirado'}), 400
    except pyjwt.InvalidTokenError:
        return jsonify({'error': 'Token inválido'}), 400
    
@app.route('/sendMailRecuperacion', methods=['POST'])
def sendMailRecuperar():
    data = request.get_json()
    smtp_server = "server.kinetica.es"  
    smtp_port = 587
    sender_email = "cuidatia@cuidatia.org"
    sender_password = "28uvy7!5U"
    receiver_email = data.get('email')

    subject = "Recuperación de contraseña"
    body = f"""
             Buenos días,

             Ha solicitado la recuperación de contraseña, pulse en el siguiente enlace para proceder:

             {FRONTEND_API_URL}recuperacion-contrasena/recuperar?m={email}
         """

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)

    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, sender_password)
            server.send_message(message)
            print("Correo enviado con éxito.")
            return jsonify({"message": "Correo enviado con éxito"}), 200
    except smtplib.SMTPAuthenticationError as e:
        print("Fallo de autenticación:", e.smtp_error.decode())
        return jsonify({"error": "Fallo de autenticación"}), 401
    except Exception as e:
        print("Otro error:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/exportarInforme', methods=['POST'])
@jwt_required()
def exportar_informe():
    
    # Establecer idioma en español
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Linux/macOS
    except locale.Error:
        locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  # Windows

    data = request.get_json()
    dataPaciente = data.get('datos')

    today = date.today()
    fecha = today.strftime('%d %B, %Y')

    # Renderizar contenido principal, header y footer
    html = render_template('pdf.html', contenido=dataPaciente, fecha=fecha)
    

    # Opciones para pdfkit
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
        'enable-local-file-access': '',  # Muy importante para rutas locales
    }

    # Generar PDF
    pdf = pdfkit.from_string(html, False, options=options)

    # Responder con el PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=informe.pdf'
    
    return response
    return jsonify({'message': 'Función de exportar informe no implementada'}), 501

@app.route('/api/getToken', methods=['POST'])
def emitir_token():
    data = request.get_json()
    entidad = data.get('entidad')
    clave = data.get('clave')

    if entidad not in ENTIDADES_EXTERNAS or ENTIDADES_EXTERNAS[entidad] != clave:
        return jsonify({"error": "Credenciales inválidas"}), 401

    # Usa create_access_token
    access_token = create_access_token(identity=entidad, expires_delta=timedelta(days=7))

    return jsonify({
        "token": access_token,
        "expira_en": "7 días"
    })
    
@app.route('/api/entities/getPacientes', methods=['GET'])
@jwt_required()
def get_all_pacientes_entities():
    try:
        pacientes = ModelPaciente.getAllPacientes(mysql)
        if not pacientes:
            return jsonify({'error': 'No se han encontrado pacientes'}), 404
        return jsonify({'message': 'Pacientes obtenidos', 'pacientes':pacientes}), 200
    except:
        return jsonify({'error':'Error al obtener los pacientes.'}), 400

@app.route('/api/sendEmail', methods=['POST'])
def send_email():
    try:
        data = request.get_json()
        to_email = data.get("to")
        print("Correo a enviar:", to_email)
        subject = data.get("subject", "Sin asunto")
        text = data.get("text", "")
        
        msg = Message(
            subject,
            recipients=[to_email],
            sender=("Cuidatia Vita", os.getenv("EMAIL_USER"))
        )
        
        msg.body = text
        msg.html = f"""
            <p>{text}</p>
        """

        mail.send(msg)

        return jsonify({"success": True, "message": "Correo enviado con éxito"})
    except Exception as e:
        print("Error enviando correo:", e)
        return jsonify({"success": False, "error": str(e)}), 500
    
@app.route('/api/sendTelegram', methods=['POST'])
def send_telegram():
    try:
        data = request.get_json()
        idPaciente = data.get("idPaciente")
        message = data.get("text", "Mensaje de prueba")

        if not idPaciente:
            return jsonify({"success": False, "error": "idPaciente no proporcionado"}), 400
        
        contactData = ModelPaciente.getContactDataPaciente(mysql, idPaciente)
        if not contactData or not contactData.get("contactTelegram"):
            return jsonify({"success": False, "error": "No se encontró contactTelegram del paciente"}), 404
        
        chat_id = contactData["contactTelegram"]

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }

        r = requests.post(url, json=payload)
        r.raise_for_status()  # lanzará error si algo falla

        return jsonify({"success": True, "message": "Mensaje enviado correctamente"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    
@app.route('/api/telegramWebhook', methods=['POST'])
def telegram_webhook():
    try:
        data = request.get_json()

        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")

            if text == "/start":
                url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
                text = (
                    f"¡Hola! Bienvenido al bot de Cuidatia Vita.\n"
                    f"Este bot notificará sobre los datos IoT del usuario, "
                    f"pero primero debes facilitar tu Chat ID a la persona a cargo de rellenar el formulario.\n"
                    f"Tu Chat ID es {chat_id}"
                )
                payload = {
                    "chat_id": chat_id,
                    "text": text
                }
                requests.post(url, json=payload)

        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/crear-meeting", methods=["POST"])
def crear_meeting():
    data = request.get_json()
    id_usuario = data.get("id_usuario")

    if not id_usuario:
        return jsonify({"error": "Falta el id_usuario"}), 400

    # Generar nombre único de sala
    nombre_canal = f"room-{uuid.uuid4().hex[:8]}"
    meet_url = f"https://meet.jit.si/{nombre_canal}"

    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO usuario_meetings (nombre_canal, url, creado_por)
            VALUES (%s, %s, %s)
            """,
            (nombre_canal, meet_url, id_usuario)
        )
        conn.commit()

        meeting_id = cursor.lastrowid

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

    finally:
        cursor.close()
        conn.close()

    return jsonify({
        "id_meeting": meeting_id,
        "nombre_canal": nombre_canal,
        "meet_url": meet_url,
        "creado_por": id_usuario
    })
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000, ssl_context=(
            "/home/ubuntu/fullchain.pem",
            "/home/ubuntu/privkey.pem"
        ))
