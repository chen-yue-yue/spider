import scrapy


class HealthNzSpider(scrapy.Spider):
    name = "health_nz"
    allowed_domains = ["health.govt.nz"]
    start_urls = ["https://health.govt.nz"]

    def parse(self, response):
        pass
