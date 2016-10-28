# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'service.kernel.RestfulConfig'


class RestfulConfig(AppConfig):
    name = 'service.kernel'
    verbose_name = _(u'核心服务')
