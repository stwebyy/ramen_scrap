# -*- coding: utf-8 -*-
import datetime
import scrapy

from ..items import RamenItem


class RamenSerachSpider(scrapy.Spider):
    name = 'ramen_search'
    allowed_domains = ['ramendb.supleks.jp']
    start_urls = ['https://ramendb.supleks.jp/search?q=%E4%BA%8C%E9%83%8E']

    def parse(self, response):
        '''

        :param response:
        :return:
        urlがある限り、parseメソッドを繰り返し行う。
        scrapy.Requestで第一引数にurl　第二引数にurlを渡す先のメソッドを指定する。
        extract_firstで指定した要素の一番目の要素を取得
        extractは指定した要素を取得。この場合は指定した要素の全てを取得するため、事前にn番目を選択する方法もある。
        '''
        ramen_data = response.css('div#contents-basic div.wrap ul#searched li')
        rank = 0
        for data in ramen_data:
            date = datetime.date.today()
            rank += 1
            rank_str = rank
            rank_str = str(rank_str) + '位'
            name = data.css('div h4 a::text').extract_first()
            url = data.css('div h4 a::attr(href)').extract_first()
            url = response.urljoin(url)
            point = data.css('div.status div.point-val::text').extract_first()
            try:
                area = data.css('div.area a::text')[2].extract()
                area = area + '駅'
            except:
                prefecture = data.css('div.area a::text').extract_first()
                city = data.css('div.area a::text')[1].extract()
                area = prefecture + city
            yield RamenItem(
                date = date,
                rank = rank_str,
                ramen_name = name,
                ramen_url = url,
                ramen_point = point,
                ramen_area = area,
            )
        return

