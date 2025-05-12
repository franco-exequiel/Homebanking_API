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
├── app/scripts/
│ └── init_db.py
├── .env
├── requirements.txt
└── README.md

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