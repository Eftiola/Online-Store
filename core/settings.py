from pathlib import Path
import os
from environs import Env



env = Env()
env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", "SuperSecret")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", [])


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users",
    "products",
    "pages",
    "categories",
    "crispy_forms",
    "crispy_bootstrap5",
    "mptt",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "core/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "products.context_processors.cart_total_amount",
                "products.context_processors.cart_total_quantity",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

_default_dburl = (BASE_DIR / "db.sqlite3").as_uri().replace("file:/", "sqlite:/")
DATABASES = {"default": env.dj_db_url("DATABASE_URL", default=_default_dburl)}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [BASE_DIR / "assets"]


MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

if DEBUG:
    INSTALLED_APPS.extend(
        [
            "django_extensions",
            "debug_toolbar",
        ]
    )

    MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1"]

MEDIA_ROOT = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


CART_SESSION_ID = "cart"


STRIPE_PUBLISHABLE_KEY = env.str("STRIPE_PUBLISHABLE_KEY", 'pk_test_51LkDf2HMG1hOZ6nUzXwP6Go2QSBil63Tc3fifFsZ3it96nPZYdpTgouKVov1bTLf5d0ihuDmkfITG2rTHLreHtrd00v0l20boY')
STRIPE_SECRET_KEY = env.str("STRIPE_SECRET_KEY",'sk_test_51LkDf2HMG1hOZ6nUV2c037ElYNiGlws83VQSSXQZ0YDTH3zG9kj7THGvR67O0jPeVOtTMVdLqBvWJSxxmBHdK5XC00af5VZ1q6')
