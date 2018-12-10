# -*- coding: utf-8 -*-
import scrapy
from myspider.spider.items import JobItem

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['lagou.com']
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.388557220.1542253747; user_trace_token=20181115115242-e7876cb9-e889-11e8-88bd-5254005c3644; LGUID=20181115115242-e7877081-e889-11e8-88bd-5254005c3644; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAIAACBID1E6484CA8620BE5BA2576B0218E5622; _gid=GA1.2.133838406.1543115011; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542854858,1542948394,1542980469,1543115011; _putrc=B17C7C318261207B123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B78511; gate_login_token=9c1dc2352e93758738e20986a2eed0527c665726716f2c2bf8a3ffe4164a2852; hasDeliver=3; LGSID=20181125203342-5811a85c-f0ae-11e8-bc7d-525400f775ce; SEARCH_ID=e17b53ea1344496b8adc6604ff412693; TG-TRACK-CODE=search_code; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543150778; LGRID=20181125210342-88991a81-f0b2-11e8-bc89-525400f775ce',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            }

    def start_requests(self):
        urls = ('https://www.lagou.com/zhaopin/{}/'.format(i) for i in range(1, 3))
        for url in urls:
            print(url)
            yield scrapy.Request(url=url,callback=self.parse,headers=self.headers)

    def parse(self, response):
        for job in response.xpath('//div[contains(@id,"s_position_list")]/ul/li'):
            salary = job.xpath('.//div[@class="p_bot"]/div[@class="li_b_l"]/span/text()').extract_first().split('-')
            ed_exp = job.xpath('.//div[@class="list_item_top"]/div/div[@class="p_bot"]/div[@class="li_b_l"]/text()').re(r'(.+)\s*/\s*(.+)')
            item = JobItem({
                'title': job.xpath('.//div[@class="position"]/div/a/h3/text()').extract_first(),
                'city': job.xpath('.//div[@class="position"]/div/a/span/em/text()').extract_first(),
                'salary_lower': salary[0],
                'salary_upper': salary[1],
                'education': ed_exp[1],
                'experience': ed_exp[0],
                'tags': job.xpath('.//div[@class="list_item_bot"]/div[@class="li_b_l"]/span/text()').extract(),
                'company': job.xpath('.//div[@class="company"]/div[@class="company_name"]/a/text()').extract_first(),
                })
            yield item

