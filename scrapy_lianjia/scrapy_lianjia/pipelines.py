# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from encodings.punycode import adapt

# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import csv



class ScrapyLianjiaPipeline:
    def __init__(self):
        """初始化Pipeline，设置CSV文件路径、计数器和字段名"""
        self.csv_file_path = "tiantongyuan.csv"
        self.item_count = 0
        self.logger = None
        # 只定义一次字段名，避免重复
        self.fieldnames = [
            "title", "tag", "total_price", "unitprice", "position",
            "house_range", "house_area", "house_toward", "house_situation",
            "house_floor", "house_year", "house_type",
            "is_near_subway", "tax_for_free", "is_anytime"
        ]

    def open_spider(self, spider):
        """爬虫启动时执行 - 只创建一次文件并写入表头"""
        self.logger = spider.logger
        self.logger.info("打开 Pipeline，准备收集数据")
        # 清空之前的文件，确保每次爬取都是新的开始
        with open(self.csv_file_path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
        self.logger.info(f"CSV文件已创建: {self.csv_file_path}")

    def process_item(self, item, spider):
        """处理每个爬取到的item - 追加模式写入数据"""
        adapter = ItemAdapter(item)
        item_dict = adapter.asdict()
        
        # 实时写入CSV，避免内存占用过大
        with open(self.csv_file_path, "a", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writerow(item_dict)
        
        self.item_count += 1
        if self.item_count % 10 == 0:
            self.logger.info(f"已写入 {self.item_count} 条房源数据")
        
        return item

    def close_spider(self, spider):
        """爬虫关闭时执行"""
        self.logger.info(f"CSV文件写入完成，共写入 {self.item_count} 条房源记录")
        self.logger.info(f"CSV文件路径: {self.csv_file_path}")
