# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from .base import BASE_DIR, DEBUG, INSTALLED_APPS

MEDIA_URL = 'http://api.gjingxi.com/media/'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'assets', 'static')
THUMB_ROOT  = os.path.join(BASE_DIR, '..', 'assets', 'media', 'thumb')
MEDIA_ROOT  = os.path.join(BASE_DIR, '..', 'assets', 'media')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
