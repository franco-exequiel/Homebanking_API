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

    ```DATABASE_URL=postgresql+asyncpg://postgres:tu_contraseña@localhost:5432/fintech_db
    ```DEBUG=true


4. Creá la base de datos fintech_db desde psql si no existe:

    ```CREATE DATABASE fintech_db;


5. Ejecutá el script para crear las tablas:

    ```bash
    ```py -m app.scripts.init_db


6. Ejecutá el servidor:
    ```bash
    ```uvicorn app.main:app --reload


## 📫 Endpoints iniciales
Método	    Ruta	    Descripción
POST	    /users	    Registrar nuevo usuario
GET	        /users	    Listar usuarios
GET	        /accounts	Ver cuenta de un usuario
POST	    /transfer	Enviar dinero (más adelante)


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