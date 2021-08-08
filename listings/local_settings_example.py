# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d3lu+*f$s-7c$6xdf-dfd(uvxd@!=#u@7f_e7df9a3a*k3#z!8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

