from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-97$%3njr*&3p9(wgz5xo)(8jj9&al9!!i!jm957e_=u@b%rp7&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # 本番環境ではFalse

ALLOWED_HOSTS = []

#ロギング設定
LOGGING = {
    'version': 1, # 1固定
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },

        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },

    },

    'handlers': {
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }


}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
