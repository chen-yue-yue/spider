# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()       # 标题
    tag = scrapy.Field()         # 标签
    total_price = scrapy.Field() # 总价
    unitprice = scrapy.Field()   # 单价
    position= scrapy.Field()    # 位置
    house_range = scrapy.Field() # 房屋格局
    house_area = scrapy.Field()  # 房屋面积
    house_toward = scrapy.Field()# 朝向
    house_situation = scrapy.Field() # 装修状态
    house_floor = scrapy.Field() # 楼层
    house_year = scrapy.Field()  # 年份
    house_type = scrapy.Field()  # 房屋类型
    is_near_subway = scrapy.Field()
    tax_for_free = scrapy.Field()
    is_anytime=scrapy.Field()
