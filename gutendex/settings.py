"""
Django settings for gutendex project.
"""

import os
import environ

# Initialize environment variables
env = environ.Env(
    ADMIN_EMAILS=(list, []),
    ADMIN_NAMES=(list, []),
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
    MANAGER_EMAILS=(list, []),
    MANAGER_NAMES=(list, []),
)

# Read from .env if it exists
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ===== SECURITY =====
SECRET_KEY = env('SECRET_KEY', default='changeme-secret-key')
DEBUG = env('DEBUG', default=False)
ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=['.onrender.com', 'localhost', '127.0.0.1'])

# ===== APPLICATIONS =====
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'corsheaders',
    'rest_framework',

    # Project apps
    'books',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gutendex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'gutendex/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gutendex.wsgi.application'

# ===== DATABASE =====
# Prefer DATABASE_URL (Render sets this automatically)
DATABASES = {
    'default': env.db(
        'DATABASE_URL',
        default='postgres:///gutendex_db_cj29'
    )
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# ===== PASSWORD VALIDATION =====
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ===== INTERNATIONALIZATION =====
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ===== STATIC & MEDIA FILES =====
STATIC_ROOT = env('STATIC_ROOT', default=os.path.join(BASE_DIR, 'staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = env('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'

# ===== EMAIL SETTINGS =====
EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER or 'no-reply@gutendex.com'

# ===== ADMINS & MANAGERS =====
ADMIN_EMAILS = env('ADMIN_EMAILS', default=[])
ADMIN_NAMES = env('ADMIN_NAMES', default=[])
ADMINS = [(ADMIN_NAMES[i], ADMIN_EMAILS[i]) for i in range(len(ADMIN_EMAILS))]

MANAGER_EMAILS = env('MANAGER_EMAILS', default=[])
MANAGER_NAMES = env('MANAGER_NAMES', default=[])
MANAGERS = [(MANAGER_NAMES[i], MANAGER_EMAILS[i]) for i in range(len(MANAGER_EMAILS))]

# ===== REST FRAMEWORK =====
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
    'PAGE_SIZE': 32,
}

# ===== CORS =====
CORS_ALLOW_ALL_ORIGINS = True

# ===== OTHER PROJECT PATHS =====
BASE_CATALOG_DIR = os.path.join(BASE_DIR, 'catalog_files')
CATALOG_RDF_DIR = os.path.join(BASE_CATALOG_DIR, 'rdf')
CATALOG_INDEX_DIR = os.path.join(CATALOG_RDF_DIR, 'index.json')
CATALOG_LOG_DIR = os.path.join(BASE_CATALOG_DIR, 'log')
CATALOG_TEMP_DIR = os.path.join(BASE_CATALOG_DIR, 'tmp')
