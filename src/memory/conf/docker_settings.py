import os
import uuid

from moccusite.conf.global_settings import *


DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() == 'true'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', str(uuid.uuid4().hex))

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')
SENTRY_JS_WHITELIST_URLS = [host.replace('.', '\.') for host in ALLOWED_HOSTS]

SECURE_COOKIES = os.environ.get('DJANGO_SECURE_COOKIES', 'True').lower() == 'true'
SESSION_COOKIE_SECURE = SECURE_COOKIES
CSRF_COOKIE_SECURE = SECURE_COOKIES

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'postgres',
        'PORT': '5432',
    }
}
