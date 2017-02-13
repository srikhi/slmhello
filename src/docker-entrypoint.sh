#!/bin/bash

# Collect static files
echo "Collect static files"
# python manage.py collectstatic --noinput

# Apply database migrations
echo "Make database migrations"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server on localhost"
# python manage.py runserver 0.0.0.0:8080
# We want all external traffic to come via locally running 
# nginx which provides ssl interface.
python manage.py runserver 8080
