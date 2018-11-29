# -*- coding: utf-8 -*-
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from annular.db import JobModel
from annular.db import Session

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        item['city'] = item['city'].split('.')[0]
        item['salary_lower'] = int(item['salary_lower'].strip('k'))
        item['salary_upper'] = int(item['salary_upper'].strip('k'))
        exp_lower,exp_upper = 0,0
        m = re.match(r'[^/d]*(/d+)-(/d+)',item['experience'])
        if m :
            exp_lower = int(m.group(1))
            exp_upper = int(m.group(2))
        tags = ''.join(item['tags'])
        jobs = JobModel(
            title = item['title'],
            cite = item['city'],
            salary_lower = item['salary_lower'],
            salary_upper = item['salary_upper'],
            experience_lower = exp_lower,
            experience_upper = exp_upper,
            education = item['education'],
            tags = tags,
            company = item['company']
                )
        self.session.add(jobs)
        return item

    def open_spider(self,spider):
        self.session = Session()

    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
