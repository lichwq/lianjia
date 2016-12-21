#usr/local/bin/python

from scrapy.cmdline import execute

def start():
     # execute(['scrapy','crawl','baixing','-o test.csv'])
     execute(['scrapy','crawl','58tongcheng'])

if __name__ == '__main__':
    start()