# 🧠 Cuidatiavita Backend

Este es el backend del proyecto **Cuidatiavita**, desarrollado con **Flask**. Gestiona la lógica de negocio de una plataforma orientada al cuidado de pacientes, organizaciones de salud y usuarios con distintos roles.

---

## 🚀 Tecnologías utilizadas

- Python 3.x
- Flask
- SQLAlchemy (ORM)
- MySQL
- Mailtrap (para testing de correos)
- Arquitectura organizada con separación entre entidades y modelos

---

## 🗂️ Estructura del proyecto

```
models/
├── entities/
│   ├── Organizacion.py
│   ├── Paciente.py
│   ├── Roles.py
│   ├── Usuario.py
|── ModelOrganizacion.py
│── ModelPaciente.py
│── ModelRoles.py
│── ModelUser.py
static/
├── img/
.env
requirements.txt
server.py
```

---

## ⚙️ Instalación y ejecución local

1. Clona el repositorio:

```bash
git clone https://github.com/Cuidatia/cuidatiavita-backend.git
cd cuidatiavita-backend
```

2. Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno en un archivo `.env` (ver ejemplo más abajo).
5. Ejecuta el servidor:

```bash
python server.py
```

El servidor se ejecutará por defecto en `http://localhost:5000`.

---



## 🗃️ Base de datos

El proyecto incluye un script SQL para crear la estructura inicial de la base de datos MySQL. Se encuentra en la carpeta `SQL/`:

📂 `SQL/cuidatiavitadb.sql`

---



## 🔐 Variables de entorno

Ejemplo de archivo `.env`:

```dotenv
# Base de datos MySQL
MYSQL_DB_HOST=localhost
MYSQL_DB_USER=root
MYSQL_DB_PASSWORD=mipassword
MYSQL_DB_NAME=cuidatiavitadb

# Servidor de correo (Mailtrap)
MAIL_HOST=sandbox.smtp.mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=93a05dc81697e8
MAIL_PASSWORD=a2c8688c98e210
MAIL_SENDER=cuidatiavita@mailtrap.io

# URL del frontend
FRONTEND_API_URL=http://localhost:3000/
```

---

## 🔌 Conexión con el Frontend

Este backend está preparado para integrarse con el frontend ubicado en:
📍 `http://localhost:3000/`

---

## 🧾 Licencia

Proyecto privado perteneciente a **Cuidatia**. No está permitido su uso sin autorización.
