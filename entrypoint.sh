#!/bin/bash
set -e

# Apply migrations
python manage.py migrate --noinput

# Create superuser if variables exist
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL || true
fi

# Execute the main command (from docker-compose.yml)
exec "$@"