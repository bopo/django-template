from __future__ import unicode_literals

import logging
from builtins import object, str

from django.db.utils import IntegrityError
from dynamic_scraper.models import SchedulerRuntime
from scrapy.exceptions import DropItem


class DjangoWriterPipeline(object):
    
    def process_item(self, item, spider):
        if spider.conf['DO_ACTION']:
            try:
                item['news_website'] = spider.ref_object
                
                checker_rt = SchedulerRuntime(runtime_type='C')
                checker_rt.save()
                item['checker_runtime'] = checker_rt
                
                item.save()
                spider.action_successful = True
                spider.log("Item saved to Django DB.", logging.INFO)
                    
            except IntegrityError as e:
                spider.log(str(e), logging.ERROR)
                raise DropItem("Missing attribute.")
                
        return item
