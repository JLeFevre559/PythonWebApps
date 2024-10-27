#!/bin/bash

# Install any new dependencies (ensure dependencies are up-to-date)
pip install -r requirements.txt

# Run migrations to apply any database changes
python manage.py migrate --noinput

# Collect static files if your app serves static files directly
python manage.py collectstatic --noinput
