from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import re
# class RunSpider(object):
    # def __init__(self):
        # print 'init'
        # process = CrawlerProcess(get_project_settings())
        # process.crawl('ipproxyspider', domain='scrapinghub.com')
        # process.start()
if __name__ == '__main__':
    # RunSpider()
    str = '<p style="display: none;">48</p>'
    str1 ='<p style="display: none;">30</p>'
    reg = '<.+ style=\"display: none;\">.{0,10}<.+>\W?'
    print re.match(reg,str1)