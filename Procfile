web: python manage.py collectstatic --noinput && python manage.py migrate && gunicorn archimedes.wsgi --bind 0.0.0.0:$PORT --log-file -
