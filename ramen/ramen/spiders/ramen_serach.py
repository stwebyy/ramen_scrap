# -*- coding: utf-8 -*-
import datetime
import scrapy

from ..items import RamenItem


class RamenSerachSpider(scrapy.Spider):
    name = 'ramen_search'
    allowed_domains = ['ramendb.supleks.jp']
    start_urls = ['https://ramendb.supleks.jp/search?q=二郎&state=tokyo&city=&order=point']

    def parse(self, response):
        '''
        メソッドのルール
        -------------------
        :param response:
        :return:
        -------------------
        概要
        -------------------
        urlがある限り、parseメソッドを繰り返し行う。-> URLがjavascriptで制御されているため、固定値で対応。10ページ目までの店舗取得。
        scrapy.Requestで第一引数にurl　第二引数にurlを渡す先のメソッドを指定する。
        extract_firstで指定した要素の一番目の要素を取得
        extractは指定した要素を取得。この場合は指定した要素の全てを取得するため、事前にn番目を選択する方法もある。
        本メソッドでは200件のラーメン店（二郎系かつ東京都）を抽出する。
        -------------------
        '''
        ramen_data = response.css('div#contents-basic div.wrap ul#searched li')
        for data in ramen_data:
            date = datetime.date.today()
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
                ramen_name = name,
                ramen_url = url,
                ramen_point = point,
                ramen_area = area,
            )
        for count in reversed(range(2, 10)):
            next_url = 'https://ramendb.supleks.jp/search?page=%s&q=二郎&state=tokyo&city=&order=point' %count
            yield scrapy.Request(next_url, callback=self.parse)
        return

