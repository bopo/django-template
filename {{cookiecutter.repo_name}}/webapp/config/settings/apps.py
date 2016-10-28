# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import INSTALLED_APPS

INSTALLED_APPS += (
    'service.frontend',
    'service.kernel',
    # 'service.wechat',
    # 'service.restauth',
    # 'service.restauth.registration',

    'imagekit',
    'reversion',
    'easy_select2',
    'import_export',
)

