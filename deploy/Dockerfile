# Usamos una imagen oficial con Python 3.11
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios
COPY ../requirements.txt .

# Instalamos dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install alembic
# Instalar netcat para esperar a PostgreSQL
RUN apt-get update && apt-get install -y netcat-openbsd

# Copiamos el resto del código
COPY .. .

# Exponemos el puerto donde correrá FastAPI (por defecto 8000)
EXPOSE 8000

# Comando por defecto para correr el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# Damos permisos al entrypoint
RUN chmod +x ./deploy/entrypoint.sh
# Comando por defecto al iniciar el contenedor
ENTRYPOINT ["./deploy/entrypoint.sh"]