import os

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kchat',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}