import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j(6s_mmpw*$*xta+8@8k_!wpt#gh)&4%$umlk+s2_8o6pquk&='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Custom apps
    'interface',
    'account',
    'pixel',
]

AUTH_USER_MODEL = 'account.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lightlab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'lightlab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS= [
    os.path.join(BASE_DIR, 'assets/')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Media settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


#Emails settings
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_USE_TLS=True
# EMAIL_HOST_USER=os.environ.get("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASS')
EMAIL_HOST_USER = 'netrobeweb@gmail.com'
EMAIL_HOST_PASSWORD = 'wpcgtxfwmiqnlbwv'
# Custom user defined mail username
# DEFAULT_FROM_EMAIL = 'info@xcrowme.com'
DEFAULT_FROM_EMAIL = 'LightLab@gmail.com'
DEFAULT_COMPANY_EMAIL = 'netrobeweb@gmail.com'


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


# Setting the stripe keys
if DEBUG:
    # test keys
    STRIPE_PUBLISHABLE_KEY = ''
    STRIPE_SECRET_KEY = ''
else:
    # live keys
    STRIPE_PUBLISHABLE_KEY = ''
    STRIPE_SECRET_KEY = ''


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'loggers': {
#         'dev': {
#             'handlers': ['dev'],
#             'level': 'DEBUG',
#         },
#         'dev.error': {
#             'handlers': ['dev_error'],
#             'level': 'WARNING',
#             'propagate': False,
#         },
#     },
#     'handlers': {
#         'dev': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': './logs/django/debugs.log',
#             'formatter' : 'simpleRe',
#         },
#         'dev_error': {
#             'level': 'WARNING',
#             'class': 'logging.FileHandler',
#             'filename': './logs/django/errors.log',
#             'formatter' : 'simpleRe',
#         },
#     },
#     'formatters':{
#         'simpleRe':{
#             'format': '{levelname}:{asctime}:{name}:{message}',
#             'style': '{',
#         }
#     }
# }