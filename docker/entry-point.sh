#!/bin/bash

PROJECT_SRC=SAFTIMS-HR-0.0.1
ACTIVATE_PATH=/src/webapp/virt/bin/activate
DJANGO_WSGI_MODULE=shinkafa.wsgi
DJANGO_SETTINGS_MODULE=shinkafa.settings


export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export ENV="prod"
django-admin migrate                  # Apply database migrations

touch /src/webapp/shinkafa/logs/gunicorn.log
touch /src/webapp/shinkafa/logs/access.log
touch /src/webapp/shinkafa/logs/nginx-access.log;
touch /src/webapp/shinkafa/logs/nginx-error.log;

tail -n 0 -f /src/webapp/shinkafa/logs/*.log &

# Restart nginx
echo Restarting Nginx
nginx -s reload
service nginx restart
# # Start Gunicorn processes
echo Starting Gunicorn
exec gunicorn shinkafa.wsgi:application \
     --name shinkafa \
     --bind=127.0.0.1:8000
     --workers 3 \
     --log-level=debug \
     --log-file=/src/webapp/shinkafa/logs/gunicorn.log \
     --access-logfile=/src/webapp/shinkafa/logs/access.log \
     "$@"



