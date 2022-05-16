#!/bin/sh

echo "Checking if database is up and ready to receive connection"
until python wait_for_db.py; do
  echo "Database is unavailable - sleeping"
  sleep 1
done

echo "Database is up and running"

echo "Creating migrations"
python manage.py makemigrations

echo "Running migration files"
python manage.py migrate

echo "Seeding sample data"
python manage.py seed

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
