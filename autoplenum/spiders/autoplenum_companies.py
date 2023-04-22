import scrapy


class AutoplenumCompaniesSpider(scrapy.Spider):
    name = "autoplenum_companies"
    allowed_domains = ["autoplenum.de"]
    start_urls = ["http://autoplenum.de/"]

    def parse(self, response):
        pass
