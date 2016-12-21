# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import string
from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors
from scrapy import log
from lianjia.cities import CITY_LIST

class JsonWithEncodingCnblogsPipeline(object):
    def __init__(self):
        #费德勒司法鉴定所捐款方式
        self.file = codecs.open('cnblogs.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()


class MySQLStoreCnblogsPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    # pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    # 将每行更新或写入数据库中
    def _do_upinsert(self, conn, item, spider):
        linkmd5id = self._get_linkmd5id(item)
        # print linkmd5id
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        conn.execute("""
                select 1 from cnblogsinfo where linkmd5id = %s
        """, (linkmd5id,))
        ret = conn.fetchone()

        if ret:
            conn.execute("""
                update cnblogsinfo set title = %s, total_price = %s, link = %s, house_type = %s, square = %s, s_price = %s, floor = %s, fitment = %s, address = %s, community = %s where linkmd5id = %s
            """, (item['title'], item['total_price'], item['url'], item['house_type'], item['square'], item['s_price'], item['floor'], item['fitment'], item['address'],item['community'], linkmd5id))
            # print """
            #    update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            # """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
        else:
            conn.execute("""
                insert into cnblogsinfo(linkmd5id, title, total_price, link, house_type, square,s_price,floor,fitment,address,community)
                values(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s)
            """, (linkmd5id, item['title'], item['total_price'], item['url'], item['house_type'],item['square'], item['s_price'], item['floor'], item['fitment'], item['address'],item['community']))
            # print """
            #    insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated)
            #    values(%s, %s, %s, %s, %s, %s)
            # """, (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now)

    # 获取url的md5编码
    def _get_linkmd5id(self, item):
        # url进行md5处理，为避免重复采集设计
        return md5(item['url']).hexdigest()

    #异常处理
    def _handle_error(self, failure, item, spider):
        log.err(failure)

class LianjiaPipeline(object):

    def __init__(self):
        self.data_files = {}

    def process_item(self, item, spider):
        city = "shanghai"
        # title = 'case'
        line = ''
        line += self.wrap_string(item['title']) + '   '
        line += self.wrap_string(item['fatie_man']) + '\n'

        # if city not in self.data_files.keys():
            # print city
            # self.data_files[city] = open('C:/lianjia/lianjia/datafile/fangtianxia_' + city + '.csv', 'wb')
        self.data_files[city] = open('D:/king.txt', 'a')

        self.data_files[city].write(line)
        self.data_files[city].flush()
        return item
    def wrap_string(self, s):
        if not s:
            return ''
        return string.replace(s.strip().strip('\n').encode('utf-8'), ',', ' ')
        # return string.replace(s.strip().strip('\n'), ',', ' ')

    def close_spider(self, spider):
        for city in CITY_LIST:
            self.data_files[city].close()