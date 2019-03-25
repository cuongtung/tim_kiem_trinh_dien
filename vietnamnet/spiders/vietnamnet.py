# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import VietnamnetItem
import re

class scrapy_vietnamnet(scrapy.Spider):
    name = "vietnamnet"
    start_urls = ['https://vietnamnet.vn/vn/giao-duc/']
    custom_settings = {
        'DEPTH_LIMIT': 2
    }
    def parse(self,response):
        title = "".join(response.xpath('//h1/text()|//h2/text()').getall())
        time = "".join(response.xpath("//span[contains(@class,'right')]/text()").getall())
        content = "".join(response.xpath("//div[@class='ArticleContent']/p/text()").getall())
        regex = re.compile(r'[\n\r\t]')
        title = regex.sub("",title)
        time =regex.sub("",time)
        time=re.findall("\d+/\d+/\d+", time)
        content = regex.sub("",content)
        item = VietnamnetItem(title = title,time=time, content= content, url=response.url)
        links = response.xpath('//a[contains(@href,".html")]/@href').extract()
        for link in links:
            l = response.urljoin(link)
            if re.search('https://vietnamnet.vn/vn/giao-duc/', l):
                    yield response.follow(link, callback=self.parse)
        yield item
