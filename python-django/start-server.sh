#!/bin/bash

cd /app/myproject
python manage.py migrate

uwsgi --chdir=/app/myproject \
    --module=myproject.wsgi:application \
    --master --pidfile=/tmp/project-master.pid \
    --processes=$WORKERS \
    --http=:8040 \
    --listen 1024 \
    --disable-logging
