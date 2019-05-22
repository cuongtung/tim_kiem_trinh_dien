# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import VietnamnetItem
import re


class scrapy_vietnamnet(scrapy.Spider):
    name = "vietnamnet"
    allowed_domains = ['vietnamnet.vn']
    start_urls = [
        # 'https://vietnamnet.vn/vn/giao-duc/',
        'https://vietnamnet.vn/vn/thoi-su/',
        # 'https://vietnamnet.vn/vn/thoi-su/chinh-tri/',
        # 'https://vietnamnet.vn/vn/cong-nghe/',
    ]
    custom_settings = {
        'DEPTH_LIMIT': 20
    }

    # def start_requests(self):
    #     for url in self.start_urls:
    #         # yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
    #         item = {}
    #         item['start_url']= url
    #         # request = Request(url, dont_filter=True)
    #         # set the meta['item'] to use the item in the next call back
    #         request = Request(url=url, callback=self.parse, dont_filter=True)
    #         request.meta['item'] = item
    #         yield request

    def parse(self, response):
        title = "".join(response.xpath('//h1/text()|//h2/text()').getall())
        time = "".join(response.xpath("//span[contains(@class,'right')]/text()").getall())
        content = "".join(response.xpath("//div[@class='ArticleContent']/p/text()").getall())
        tags = response.xpath('.//div[@id="BoxTag"]//ul[@class="clearfix"]/li/a/text()').extract()

        regex = re.compile(r'[\n\r\t]')
        title = regex.sub("", title)
        time = regex.sub("", time)
        time = re.findall("\d+/\d+/\d+", time)
        content = regex.sub("", content)

        item = VietnamnetItem(title=title, time=time, content=content, url=response.url, tags=tags)

        links = response.xpath('//a[contains(@href,".html")]/@href').extract()

        # url = response.request.url
        for link in links:
            l = response.urljoin(link)
            if re.search('https://vietnamnet.vn/vn/thoi-su/', l):
                yield response.follow(link, callback=self.parse)
        yield item
