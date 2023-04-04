#!/bin/bash
python3 manage.py migrate
gunicorn --bind 0.0.0.0:5000 --timeout=300 -k gevent webscrapper.wsgi