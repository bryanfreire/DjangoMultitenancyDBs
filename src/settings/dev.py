from settings._base import *


# Custom functions

def get_postgres_db(name):
    return {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': name,
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432,
    }


# Databases

DATABASES.update({
    'auth': get_postgres_db('auth'),
    'earth': get_postgres_db('earth'),
    'mars': get_postgres_db('mars'),
})
