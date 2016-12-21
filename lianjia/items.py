# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class lianjiaitem(scrapy.Item):
    # city = scrapy.Field()
    title = scrapy.Field()
    total_price = scrapy.Field()
    house_type = scrapy.Field()
    square = scrapy.Field()
    s_price = scrapy.Field()
    floor = scrapy.Field()
    fitment = scrapy.Field()
    url = scrapy.Field()
    address = scrapy.Field()
    community = scrapy.Field()
    # rent = scrapy.Field()
    # payType = scrapy.Field()
    # villageName = scrapy.Field()
    # address = scrapy.Field()
    # phone = scrapy.Field()
    # publish_time = scrapy.Field()
    # crawled_time = scrapy.Field()