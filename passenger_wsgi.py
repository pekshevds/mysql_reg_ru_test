import os, sys
sys.path.insert(0, '/var/www/u0872810/data/www/klaringl.annasoft.site/server')
sys.path.insert(1, '/var/www/u0872810/data/www/klaringl.annasoft.site/.venv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
