"""
Django settings for ljhub project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '8000-ljtalks-ljhub-at6xms91as2.ws.codeinstitute-ide.net', 'ljhub-b444eee3873a.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # Admin panel
    'django.contrib.auth',  # Authentication system
    'django.contrib.contenttypes',  # Content types framework
    'django.contrib.sessions',  # Session management
    'django.contrib.messages',  # Messaging framework
    # Statics; should be before apps that manage static files
    'django.contrib.staticfiles',
    # Can go anywhere. # Required for managing multiple sites and for django-allauth integration
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # This goes after django and allauth files as it overrides the default static file storage
    'cloudinary_storage',
    'cloudinary',  # Image management. Should be after cloudinary_storage
    'crispy_forms',
    'crispy_bootstrap5',
    'django_summernote',  # Rich text editor for admin
    'blog',  # My custom apps come after django then third-party apps
    'ljhub',
    'notes',
    'products',
    'user_profile',
]

CRISPY_ALLOWED_TEMPLATE_PACKs = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Site framework ID - required for django.contrib.sites
SITE_ID = 1  # So Django can handle multiple sites from one database
LOGIN_REDIRECT_URL = '/'  # returns user to home page after logging in
LOGOUT_REDIRECT_URL = '/'  # returns user to home page after logging out
ACCOUNT_SIGNUP_REDIRECT_URL = '/'  # Unless redirected with Next, go to blog list

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Adds additional functionality to the projects account user authentication
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'ljhub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ljhub.context_processors.support_email'
            ],
        },
    },
]

WSGI_APPLICATION = 'ljhub.wsgi.application'


DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com"
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.NumericPasswordValidator'),
    },
]

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = True
# ACCOUNT_TEMPLATE_EXTENSION

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Dev
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Prod
EMAIL_HOST = 'mail.privateemail.com'
EMAIL_PORT = 465  # or 587 depending on your provider
EMAIL_USE_SSL = True  # or False if using SSL
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
SUPPORT_EMAIL = os.getenv('SUPPORT_EMAIL')

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configure Whitenoise to handle static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media file handling (Images and uploads)
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
