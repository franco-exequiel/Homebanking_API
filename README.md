# 🏦 Fintech API – HomeBanking Backend

API RESTful construida con **FastAPI** y **PostgreSQL** para simular un sistema básico de homebanking.  
Permite registrar usuarios, asociarles cuentas, realizar transferencias y consultar transacciones.

---

## 🚀 Tecnologías

- **Python 3.11+**
- **FastAPI** – Web framework moderno
- **PostgreSQL** – Base de datos relacional
- **SQLAlchemy + AsyncPG** – ORM asíncrono
- **Pydantic** – Validación de datos
- **Dotenv** – Manejo de variables de entorno

---

## 📁 Estructura del proyecto

fintech_api/
├── app/
│ ├── main.py
│ ├── config.py
│ ├── database.py
│ ├── models/
│ │ ├── user.py
│ │ └── account.py
│ ├── schemas/
│ │ ├── user.py
│ │ └── account.py
│ ├── routes/
│ │ ├── users.py
│ │ └── accounts.py
│ ├── services/
│ │ └── auth.py
├── alembic/
│ ├── env.py
│ └── script.py.mako
├── tests/
│ └── test_users.py
├── deploy/
│ ├── Dockerfile
│ ├── docker-compose.yml
│ ├── .dockerignore
│ └── entrypoint.sh 
├── .env
├── .gitignore
├── requirements.txt
└── README.md
└── alembic.ini

---

## ⚙️ Configuración

1. Cloná el repositorio:
   ```bash
   ```git clone https://github.com/tu_usuario/fintech_api.git
   ```cd fintech_api


2. Instalá las dependencias:

    ```bash
    ```pip install -r requirements.txt


3. Configurá el archivo .env:

    ``` 'DATABASE_URL=postgresql+asyncpg://postgres:tu_contraseña@localhost:5432/fintech_db'
    ```DEBUG=true


4. Creá la base de datos fintech_db desde psql si no existe:
    
    ```bash
    ```psql
    ```CREATE DATABASE fintech_db;

5. Ejecutá el script para crear las tablas:

    ```bash
    ```py -m app.scripts.init_db


6. Ejecutá el servidor:
    ```bash
    ```uvicorn app.main:app --reload


## 📫 Endpoints iniciales
### Método: GET
Rutas:
/users -> Listar Usuarios
/accounts -> Ver cuenta de un usuario

### Método: POST
Rutas:
/users -> Registrar nuevo usuario
/transfer -> Enviar dinero (En progreso)


## 📘 Alembic & Migraciones – Configuración y Uso
### 🔧 Configuración de Alembic
Este proyecto usa SQLAlchemy en modo asincrónico (asyncpg) para la app, pero Alembic requiere una conexión sincrónica (psycopg2) para autogenerar migraciones.

Por eso:
* alembic.ini contiene un placeholder en sqlalchemy.url.
* La conexión real a la base de datos se obtiene desde el archivo .env.

📂 .env
Asegurate de tener un archivo .env en la raíz del proyecto con al menos esta variable:
    
    ```bash
    ```DATABASE_URL=postgresql+asyncpg://usuario:password@localhost:5432/tu_base
Alembic convertirá internamente esta URL a psycopg2 para poder conectarse en modo sincrónico.

### 🧠 ¿Por qué no se usa async en Alembic?
SQLAlchemy async (async_engine) no es compatible con Alembic directamente, ya que Alembic se ejecuta de forma sincrónica.
Para resolver esto, en alembic/env.py se realiza una transformación automática de la URL de conexión:

```bash
```import os
    from dotenv import load_dotenv

    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL").replace("asyncpg", "psycopg2")
    config.set_main_option("sqlalchemy.url", DATABASE_URL)
```
Esto permite que Alembic se conecte sincrónicamente solo para inspeccionar el esquema y generar migraciones.


## 🐳 Docker y Docker Compose
Para facilitar el despliegue del proyecto HomeBanking_API, se utilizó Docker para contenerizar la aplicación y PostgreSQL como base de datos. Toda la configuración se encuentra dentro de la carpeta infraestructure/.

### 📁 Estructura Docker
deploy/
├── Dockerfile                # Imagen de la API en FastAPI
├── docker-compose.yml        # Orquestación de contenedores
├── .dockerignore             # Exclusión de archivos innecesarios para la imagen
└── entrypoint.sh             # Se ejecuta automáticamente con la configuración correspondiente cuando se levanta el contenedor

### ⚙️ Dockerfile
El Dockerfile construye una imagen de la API, basada en Python, instalando dependencias desde requirements.txt y exponiendo el servicio en el puerto 8000.

### 🧪 docker-compose.yml
Este archivo define dos servicios:
* web: contenedor que corre la API con Uvicorn
* db: contenedor de PostgreSQL (usando la imagen oficial, versión 17)

Ambos servicios comparten una red Docker y usan volúmenes persistentes para la base de datos.

```bash
services:
  web:
    build:
      context: ..
      dockerfile: infraestructure/Dockerfile
    ports:
      - "8000:8000"
    env_file:
      - ../.env
    depends_on:
      - db

  db:
    image: postgres:17
    environment:
      POSTGRES_DB: fintech_db
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```
### 🔒 Variables de Entorno
La configuración sensible (como credenciales de la base de datos) se carga desde el archivo .env, que no debe subirse al repositorio. Asegurate de tenerlo en el mismo nivel que docker-compose.yml.

```bash
POSTGRES_USER=usuario
POSTGRES_PASSWORD=contraseña
DATABASE_URL=postgresql+asyncpg://usuario:contraseña@db:5432/nombre_db
```



## ✍️ Autor
Franco Exequiel Fernández
📧 [Gmail:](frexe007@gmail.com)
🔗 [LinkedIn:](https://www.linkedin.com/in/franco-exequiel)



## ✅ Próximos pasos
 Autenticación (login con JWT)

 Transferencias entre cuentas

 Historial de movimientos

 Tests con Pytest

 Contenerización con Docker