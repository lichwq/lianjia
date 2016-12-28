#coding=utf-8

import scrapy
import re
import time
import random
# from scrapy import Request


from lianjia.items import lianjiaitem
from lianjia.cities import CITY_LIST


class DmozSpider(scrapy.Spider):
    name = "58tongcheng"
    #xiugai

    allowed_domains = ["lianjia.com"]
    #可允许域名列表

    # start_urls = ["http://sh.58.com/chuzu"]
    # start_urls = map(lambda city: 'http://' + city + '.58.com/dog/', CITY_LIST)
    start_urls = ["http://sh.lianjia.com/ditiefang/d2g1"]
    #请求url列表
    # print start_urls

    def parse(self,  response):

        img_rows = response.xpath("//div[@class='list-wrap']/ul[@id='house-lst']/li/div[@class='info-panel']/h2/a")

        print img_rows

        for row in img_rows:
            url = self.first(row.xpath("@href").extract())
            # print url
            # print response.urljoin(url)
            # print response
            yield scrapy.Request(response.urljoin(url), callback=self.parse_detail)

        next_page_word = u"下一页"
        # next_page = response.xpath('//a[text()="%s"]/@href' % next_page_word) .extract()
        next_page = response.xpath('//div[@class="con-box"]/div[@class="page-box house-lst-page-box"]/a[text()="%s"]/@href' % next_page_word).extract()

        if next_page:
            yield scrapy.Request(response.urljoin(next_page[0]), callback=self.parse)

    def parse_detail(self, response):

        # city = 'sh'
        # city = self.fromUrl(response.url)
        # phone = response.xpath("//h1/text()")
        # print phone
        # print response.url

        # fatie_man = response.xpath("//div[@id='t_main']/div[@class='bbs_head']/div[@class='bbs-hd-h1']/h1[@id='j_data']/text()")
        # title = response.xpath("//div[@id='tpc']//div[@class='floor_box']/div[@class='author']/div[@class='left']/a[@class='u']/text()")
        # level = response.xpath("//div[@class='author']/div[@class]/span[@class]/a/text()")

        title = response.xpath("//div[@class='content']/div[@class='title']/h1[@class='main']/text()")
        total_price = response.xpath("//div[@class='houseInfo']/div[@class='price']/div[@class='mainInfo bold']/text()")
        house_type = response.xpath("//div[@class='content']/div[@class='houseInfo']/div[@class='room']/div[@class='mainInfo']/text()")
        house_type_s = response.xpath("//div[@class='content']/div[@class='houseInfo']/div[@class='room']/div[@class='mainInfo']/span/text()")
        square = response.xpath("//div[@class='content']/div[@class='houseInfo']/div[@class='area']/div[@class='mainInfo']/text()")
        s_price = response.xpath("//div[@class='content']/table[contains(@class,'aroundInfo')]//tr[1]/td/text()")
        floor = response.xpath("//div[@class='cj-cun']/div[@class='content']/table[contains(@class,'aroundInfo')]//tr[2]/td[1]/text()")
        fitment = response.xpath("//div[@class='content']/table[contains(@class,'aroundInfo')]//tr[3]/td[1]/text()")
        address_x = response.xpath("//div[@id='zoneMap']/@latitude")
        address_y = response.xpath("//div[@id='zoneMap']/@longitude")
        address = response.xpath("//div[@class='content']/table[contains(@class,'aroundInfo')]//tr[6]/td/p[@class='addrEllipsis fl ml_5']/@title")
        community = response.xpath("//table[contains(@class,'aroundInfo')]//tr[5]/td/a[@class='propertyEllipsis ml_5']/text()")

        # rent = response.xpath("//section[contains(@class,'viewad-meta')]/ul/li/span[0]/text()")
        # payType = response.xpath("//section[contains(@class,'viewad-meta')]/ul/li/span[1]/text()")
        # villageName = response.xpath("//section[contains(@class,'viewad-meta')]/ul/li/span[contains(@class,'meta-小区名')]/text()")
        # address = ''.join(response.xpath("//section[contains(@class,'viewad-meta')]/ul/li/span[contains(@class,'meta-address')]//text()").extract())
        # publish_time = response.xpath("//div[contains(@id,'viewad-actions')]/span[contains(@data-toggle,'tooltip')]/test()")


        if title:
            item = lianjiaitem()
            item['url'] = response.url
            item['title'] = self.first(title.extract())
            item['total_price'] = self.first(total_price.extract())
            item['house_type'] = self.first(house_type.extract()).strip()+self.first(house_type_s.extract()).strip()+self.second(house_type.extract()).strip()+self.second(house_type_s.extract()).strip()
            item['square'] = self.first(square.extract())
            item['s_price'] = self.second(s_price).extract().strip()
            item['floor'] = self.second(floor).extract().strip()
            item['fitment'] = self.second(fitment).extract().strip()
            item['address'] = self.first(address.extract())
            item['community'] = self.first(community.extract())+"["+self.first(address_x.extract())+","+self.first(address_y.extract())+"]"


            print item['url']
            print item['title']
            print item['total_price']
            print item['house_type']
            print item['square']
            print item['s_price']
            print item['floor']
            print item['fitment']
            print item['address']
            print item['community']

            # item['city'] = city
            # print item['city']
            return item

    def first(self, l):
        if len(l):
            return l[0]
        return 'null'

    def second(self, l):
        if len(l):
            return l[1]
        return 'null'


    # def fromUrl(self, url):
    #     match_result = re.match(r'^http://zu.(\w+)\.fang.com/', url, re.M | re.I)
    #     return match_result.group(1)