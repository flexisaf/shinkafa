#!/bin/bash


echo Starting Gunicorn
exec gunicorn shinkafa.wsgi:application \
     --name hrms \
     --bind=127.0.0.1:8000
     --workers 3 \
     --log-level=debug \




