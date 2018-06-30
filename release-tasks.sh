#!/usr/bin/env bash

echo Migrate
python manage.py migrate

echo Creating users
python create_user.py