#!/bin/bash

./manage.py collectstatic --noinput

./manage.py migrate

./manage.py runserver
