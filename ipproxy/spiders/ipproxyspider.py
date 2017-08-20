# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.http import FormRequest
from ipproxy.items import IpproxyItem
from scrapy.selector import Selector
import time, urllib,re
class fangong(Spider):
    name = 'ipproxyspider'
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    current_time = unicode(str(time.strftime('%Y-%m-%dT%H:%M:%S')+'+08:00'))
    page_index = 0
    download_delay = 2
    def start_requests(self):
        yield FormRequest('http://www.goubanjia.com/free/index.shtml',callback=self.parse_page,headers=self.headers,dont_filter = True)
    def parse_page(self,response):
        self.page_index+=1
        print response.url
        # // td[ @class =\'ip\']/div/text()
        tables = response.xpath('//tbody/tr').extract()
        for line  in tables:
            item = IpproxyItem()
            reg = '<.+ style=\"display: none;\">.{0,10}<.+>'
            num = 'style="display: none;"'
            ips = Selector(text=line).xpath('//td[@class=\'ip\']/*').extract()
            for single in ips:
                print single.strip()
                print single.index(num)
            ip_div =  Selector(text=line).xpath('//div/text()').extract()
            # print ip_span
            # print ip_div
            # print line

            print '=================================================================='
        yield FormRequest('http://www.goubanjia.com/free/index'+str(self.page_index)+'.shtml',callback=self.parse_page,headers=self.headers,dont_filter = True)
    def parse_item(self, response):
        item = IpproxyItem()
        item['url'] = response.url
        yield item
    def parse_time(self, item_time):
        return time.strftime("%Y-%m-%d", time.strptime(item_time, '%m/%d/%Y'))
    def get_request_time(self,x):
        return urllib.quote(time.strftime('%Y-%m-%dT%H:%M:%S+08:00',x))
