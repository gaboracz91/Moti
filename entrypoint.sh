#!/usr/local/bin/dumb-init /bin/sh

if [ "$MODE" = 'eu-production' ]; then
    echo "Running in prod"
    export DJANGO_SETTINGS_MODULE='project.settings.prod'

else
    echo "Running in dev"
    export DJANGO_SETTINGS_MODULE='project.settings.dev'
fi

python manage.py migrate
python manage.py collectstatic --clear --noinput
python manage.py collectstatic --noinput

echo Creating users
python create_user.py

echo Starting Gunicorn.
gunicorn project.wsgi --name im-ok-core-service --bind :8080 --workers 3 --access-logfile "-" --error-logfile "-"
