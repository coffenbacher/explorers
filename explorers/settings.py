import os
import sys

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage') # 'bjjweb.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE', 'django.contrib.staticfiles.storage.StaticFilesStorage') # 'bjjweb.s3utils.StaticRootS3BotoStorage'

#FIX AWS_ACCESS_KEY_ID = 'AKIAI3APQKONXVPX26XA'
#FIX AWS_SECRET_ACCESS_KEY = '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'
#FIX AWS_STORAGE_BUCKET_NAME = 'bjjweb'

if 'StaticFilesStorage' in STATICFILES_STORAGE:
    STATIC_ROOT = os.path.join(PROJECT_PATH, '../staticfiles')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
    MEDIA_URL = '/media/'
else:
    S3_URL = 'http://s3-us-west-2.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
    STATIC_ROOT = '/static/'
    STATIC_URL = S3_URL + STATIC_ROOT
    MEDIA_ROOT = '/media/'#os.path.join(PROJECT_PATH, 'media')
    MEDIA_URL = S3_URL + MEDIA_ROOT
    #MEDIA_UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'uploads')


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = '@7pw1!g$-f8#eqy7=&amp;ys++ztzn_u4=2q6xw_1*3z_zo%n$*z)+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'explorers.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'explorers.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, '../templates'),
)

INSTALLED_APPS = (
    'gunicorn',
    'south',
    'storages',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'explorers',
    'django.contrib.admin',
    'django.contrib.admindocs',
#    'fixture_magic',
#    'django_extensions',
#    'django_extensions.tests',
#    'photologue',
#    'registration',
#    'bjjprofile',
#    'technique',
#    'flow',
#    'competition'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Parse database configuration from $DATABASE_URL
db = {'username': 'postgres',
      'password': 'beffy44',
      'name': 'explorers',}

import dj_database_url
DATABASES['default'] = dj_database_url.config(
                        default='postgres://%s:%s@localhost:5432/%s' % (
                                db['username'], 
                                db['password'], 
                                db['name'])
                        )

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/users/'

TEST_RUNNER = 'ignoretests.DjangoIgnoreTestSuiteRunner'
IGNORE_TESTS = (
    'storages',
    'registration'
)
