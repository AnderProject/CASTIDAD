#!/usr/bin/venv bash

set -o errexit

pip install -r requeriments.txt

python manage.py collectstatic -- noinput
python manage.py migrate