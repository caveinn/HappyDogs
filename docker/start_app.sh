#!/bin/bash

source /root/.local/share/virtualenvs/happy-dogs*/bin/activate

echo "<<<<<<<< Collect Staticfiles>>>>>>>>>"
python manage.py collectstatic --noinput


sleep 14
echo "<<<<<<<< Database Setup and Migrations Starts >>>>>>>>>"
# Run database migrations
python manage.py migrate &

sleep 5
echo "<<<<<<< Database Setup and Migrations Complete >>>>>>>>>>"
echo " "

echo "<<<<<<<<<<<<<<<<<<<< START APP >>>>>>>>>>>>>>>>>>>>>>>>"
# python manage.py runserver 0.0.0.0:8000
# Start the APP with gunicorn
gunicorn --bind 0.0.0.0:8000 app.wsgi --reload --access-logfile '-' --workers=2
