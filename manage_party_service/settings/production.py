from manage_party_service.settings.base import *

DEBUG = get_environment_var('DEBUG', 'False') == 'True'

TESTING = False

SERVICE_DOMAIN = 'https://mps.sepid.org'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_environment_var('DB_NAME'),
        'USER': get_environment_var('DB_USER', 'user'),
        'PASSWORD': get_environment_var('DB_PASS'),
        'HOST': get_environment_var('DB_HOST'),
        'PORT': get_environment_var('DB_PORT', '5432')
    }
}

LOG_LEVEL = get_environment_var('LOG_LEVEL', 'INFO')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)-8s [%(module)s:%(funcName)s:%(lineno)d]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'logging/debug.log'),
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': LOG_LEVEL,
            'propagate': True
        },
        'django': {
            'handlers': ['file', 'console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'manage_party_service': {
            'handlers': ['file', 'console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
    },
}

SWAGGER_URL = f'{SERVICE_DOMAIN}api/'

SECRET_KEY = get_environment_var(
    'SECRET_KEY', '*z!3aidedw32xh&1ew(^&5dgd17(ynnmk=s*mo=v2l_(4t_ff(')

CSRF_TRUSTED_ORIGINS = get_environment_var(
    'CSRF_TRUSTED_ORIGINS', '*').split(',')

ALLOWED_HOSTS = get_environment_var('ALLOWED_HOSTS', '*').split(',')
