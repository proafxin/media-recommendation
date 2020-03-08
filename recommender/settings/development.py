from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': data['DATABASE_HOST'],
        'NAME': data['DATABASE_NAME'],
        'USER': data['DATABASE_USER'],
        'PASSWORD': data['DATABASE_PASSWORD'],
        'PORT': data['DATABASE_PORT'],
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    }
}

STATIC_ROOT = join(BASE_DIR, 'static/')
MEDIA_ROOT = join(BASE_DIR, 'media/')
CRISPY_TEMPLATE_PACK = 'bootstrap4'