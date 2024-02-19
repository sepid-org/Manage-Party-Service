#!/bin/bash

python3 ./manage.py collectstatic --noinput --clear

python3 ./manage.py migrate

python3 ./manage.py runserver