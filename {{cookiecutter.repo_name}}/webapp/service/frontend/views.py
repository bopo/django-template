# -*- coding: utf-8 -*-

from django.shortcuts import render

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


# @cache_page(60 * 15)
def home(request):
    return render(request, 'home/index.html', locals())
