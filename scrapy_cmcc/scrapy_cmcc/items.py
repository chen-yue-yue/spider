# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyCmccItem(scrapy.Item):
    case_id = scrapy.Field()
    num = scrapy.Field()
    case_title = scrapy.Field()
    translate_name = scrapy.Field()
    writer = scrapy.Field()
    workplace = scrapy.Field()
    director = scrapy.Field()
    translate_worker = scrapy.Field()
    company = scrapy.Field()
    industry = scrapy.Field()
    large = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    work_page = scrapy.Field()
    case_type = scrapy.Field()
    chinese_keywords = scrapy.Field()
    english_keywords = scrapy.Field()
    chinese_digest = scrapy.Field()
    english_digest = scrapy.Field()
    right_object = scrapy.Field()
    measure = scrapy.Field()
    years = scrapy.Field()
    course = scrapy.Field()
    knowledge = scrapy.Field()
    time = scrapy.Field()
    total = scrapy.Field()
    explanation = scrapy.Field()
    english_original = scrapy.Field()
    english_explanation = scrapy.Field()
