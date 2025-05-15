#!/bin/bash

# Salir si algo falla
set -e

echo "📦 Esperando a que la base de datos esté lista..."

# Espera activa hasta que PostgreSQL esté disponible
until nc -z db 5432; do
  sleep 1
done

echo "✅ Base de datos disponible."

echo "🔍 DATABASE_URL=$DATABASE_URL"

echo "🔄 Ejecutando migraciones con Alembic..."
alembic upgrade head

echo "🚀 Iniciando FastAPI con Uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000