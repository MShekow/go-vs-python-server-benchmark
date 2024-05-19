#!/bin/bash

cd /app/myproject
python manage.py migrate

python main.py
