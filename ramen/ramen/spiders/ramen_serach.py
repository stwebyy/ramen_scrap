# -*- coding: utf-8 -*-
import scrapy


class RamenSerachSpider(scrapy.Spider):
    name = 'ramen_search'
    allowed_domains = ['ramendb.supleks.jp']
    start_urls = ['https://ramendb.supleks.jp']

    def parse(self, response):
        ramen_data = response.css('div h4 a::text').extract_first()
        print(ramen_data)