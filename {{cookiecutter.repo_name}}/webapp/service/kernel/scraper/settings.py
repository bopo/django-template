from __future__ import unicode_literals

import os
import sys

# Scrapy settings for service.project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
sys.path.insert(0, os.path.join(PROJECT_ROOT, "../../..")) #only for example_project


BOT_NAME = 'stock'

LOG_STDOUT = True

SPIDER_MODULES = ['dynamic_scraper.spiders', 'service.scraper',]
USER_AGENT = '{b}/{v}'.format(b=BOT_NAME, v='1.0')

ITEM_PIPELINES = {
    'dynamic_scraper.pipelines.DjangoImagesPipeline': 200,
    'dynamic_scraper.pipelines.ValidationPipeline': 400,
    'service.scraper.pipelines.DjangoWriterPipeline': 800,
}

IMAGES_STORE = os.path.join(PROJECT_ROOT, '../thumbnails')

IMAGES_THUMBS = {
    'medium': (50, 50),
    'small': (25, 25),
}

DSCRAPER_IMAGES_STORE_FORMAT = 'ALL'

DSCRAPER_LOG_ENABLED = True
DSCRAPER_LOG_LEVEL = 'INFO'
DSCRAPER_LOG_LIMIT = 5
