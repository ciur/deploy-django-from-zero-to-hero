from .base import *

DEBUG = False
INTERNAL_IPS = [ '127.0.0.1', ]

ALLOWED_HOSTS = ['localhost', 'demo.dglte.net', ]

SITE_ID = 1
SECRET_KEY = os.environ['SECRET_KEY']
MEDIA_ROOT = "/home/john/media"
STATIC_ROOT = '/home/john/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN = os.environ['AWS_S3_CUSTOM_DOMAIN']
