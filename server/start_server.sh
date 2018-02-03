#!/bin/bash
[ ! -d venv ] && {
        echo "No se ha encontrado en venv. Puede crearlo con ./update_virtualenv.sh"
        exit 1
}

[ ! -f manage.py ] && {
        echo "No se ha encontrado  src/manage.py. Debe crear el proyecto Django dentro de la carpeta src"
        exit 1
}

source ./venv/bin/activate.fish
python manage.py runserver 0.0.0.0:8000 --insecure
