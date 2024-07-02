#!/bin/bash

# Aplicar las migraciones de la base de datos
echo "Applying database migrations..."
python manage.py migrate

# Recoger archivos estáticos (opcional)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Iniciar Gunicorn
echo "Starting Gunicorn..."
gunicorn negocio_usuarios.wsgi --log-file -
