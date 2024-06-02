import os, ssl
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import environ
import dj_database_url

# Deshabilitar la verificación SSL
ssl._create_default_https_context = ssl._create_unverified_context

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env( 
    DEBUG=(bool, False)
)
#Leer archivo env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

                     
# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_recaptcha",
    "captcha", 
    'rest_framework',
    'corsheaders',
    'coreapi',
    "appmanager",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "App.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                'django.template.context_processors.static',
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = "App.wsgi.application"

DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default=env('DATABASE_URL'),
        conn_max_age=600
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

TIME_ZONE = "UTC"

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
    ('pt', 'Português'),
]

LANGUAGE_CODE = "es"

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'), # Directorio para archivos de traducción personalizados
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# VARIBALES DE REDIRECCION DE LOGIN Y LOGOUT
LOGIN_REDIRECT_URL = 'adminpage'
LOGOUT_REDIRECT_URL = 'home'

AUTH_USER_MODEL = 'appmanager.Usuario'

# Configuración de sesión
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_NAME = 'mi_sesion'
SESSION_COOKIE_AGE = 1209600  # Tiempo de vida de la sesión en segundos (por defecto, 2 semanas)



RECAPTCHA_PUBLIC_KEY = '6LewjxMpAAAAALEkAWvKRj-33lg1VM6OBmrdnzc7'
RECAPTCHA_PRIVATE_KEY = '6LewjxMpAAAAAD8zH1U1mboETeUaWZRfR01AZRF6'

#Listado de urls que pueden acceder a la API
#http://localhost:5173 corresponde al servidor del vite+react
CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]

#Genera la documentacion de forma automatica del funcionamiento de la API
REST_FRAMEWORK = {
    ...: ...,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}
