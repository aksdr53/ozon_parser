import scrapy

class OsSpider(scrapy.Spider):
    name = 'ozon'
    start_urls = 'https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?sorting=rating'

    def parse(self, response):
