from memory.conf.global_settings import *


SECRET_KEY = 'dev'
ALLOWED_HOSTS = ['localhost']

DEBUG = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'memory-backend',
    }
}
