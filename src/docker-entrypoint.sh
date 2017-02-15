#!/bin/bash

echo "Creating Initial admins"
python manage.py create-admins

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Make database migrations"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

# Start server
# echo "Starting server on localhost 127.0.0.1"
# We want all external traffic to come via locally running 
# nginx which provides ssl interface.
# python manage.py runserver 127.0.0.1:80

echo "Starting server on port 80"
python manage.py runserver 0.0.0.0:80
