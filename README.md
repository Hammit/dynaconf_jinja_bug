# Description

Settings are split into various files. The entrypoint (for --settings or DJANGO_SETTINGS_MODULE) is development.py, which loads base.py
a json and yaml file. The problem is in the json file with the use of Jinja

Run Django runserver to see the problem on startup

    <path_to_venv/bin/python3 ./manage.py runserver --settings django42_dynaconf_jinja.development


