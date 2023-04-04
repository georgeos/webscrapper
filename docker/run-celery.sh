#!/bin/bash
python3 -m celery -A webscrapper worker -E -l info