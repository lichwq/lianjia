# -*- coding: utf-8 -*-

BOT_NAME = 'lianjia'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['lianjia.spiders']
NEWSPIDER_MODULE = 'lianjia.spiders'

# COMMANDS_MODULE = 'lianjia.commands'
# USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# Obey robots.txt rules


# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'lianjia.middlewares.RandomUserAgent': 1, #随机user agent
    # 'lianjia.middlewares.ProxyMiddleware': 2, #随机proxy
    # 'scrapy_crawlera.CrawleraMiddleware': 600, #crawlera代理用到
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'lianjia.pipelines.BaixingPipeline': 200,
    'lianjia.pipelines.MySQLStoreCnblogsPipeline': 200
}

COOKIES_ENABLED = False #cookies是否启用
CONCURRENT_REQUESTS = 16 #并发数量
RETRY_ENABLED = False #是否重试
DOWNLOAD_DELAY = 0.1  #请求下载延时
DOWNLOAD_TIMEOUT = 15  #下载超时设定
REDIRECT_ENABLED = False #是否重定向
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'INFO' #日志级别

# start MySQL database configure setting
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'jr_test'
MYSQL_USER = 'root'
MYSQL_PASSWD = '198982asd'
# end of MySQL database configure setting

USER_AGENTS = [
    # "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    # "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    # "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    # "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    # "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    # "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    # "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    # "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    # "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    # "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    # "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    # "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    # "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    # "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

PROXIES = [
	{'ip_port': '122.72.32.72:80', 'user_pass': ''},
	{'ip_port': '120.198.243.22:80', 'user_pass': ''},
	{'ip_port': '111.8.60.9:8123', 'user_pass': ''},
	{'ip_port': '101.71.27.120:80', 'user_pass': ''},
	{'ip_port': '122.96.59.104:80', 'user_pass': ''},
	{'ip_port': '122.224.249.122:8088', 'user_pass': ''},
]