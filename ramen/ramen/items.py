# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RamenItem(scrapy.Item):
    date = scrapy.Field()
    rank = scrapy.Field()
    ramen_name = scrapy.Field()
    ramen_url = scrapy.Field()
    ramen_point = scrapy.Field()
    ramen_area = scrapy.Field()
    pass
