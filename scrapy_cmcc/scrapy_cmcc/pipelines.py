from itemadapter import ItemAdapter
import csv

class ScrapyCmccPipeline:
    def open_spider(self, spider):
        spider.logger.info("打开 Pipeline，准备实时写入 CSV（中文表头）")
        self.file = open("cmcc_cases_cn.csv", "w", encoding="utf-8-sig", newline="")
        self.fieldnames = [
            'case_id', 'num', 'case_title', 'translate_name', 'writer', 'workplace',
            'director', 'translate_worker', 'company', 'industry', 'large', 'area',
            'language', 'work_page', 'case_type', 'chinese_keywords', 'english_keywords',
            'chinese_digest', 'english_digest', 'right_object', 'measure', 'years',
            'course', 'knowledge', 'time', 'total', 'explanation', 'english_original',
            'english_explanation'
        ]
        self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        # 只写一次中文表头
        self.writer.writerow({
            'case_id': '案例编号',
            'num': '被浏览次数',
            'case_title': '案例名称',
            'translate_name': '译名',
            'writer': '案例作者',
            'workplace': '作者单位',
            'director': '指导者',
            'translate_worker': '译者',
            'company': '案例企业名称',
            'industry': '行业',
            'large': '规模',
            'area': '案例涉及的职能领域',
            'language': '案例语种',
            'work_page': '案例正文页数（页）',
            'case_type': '案例类型',
            'chinese_keywords': '中文关键词',
            'english_keywords': '英文关键词',
            'chinese_digest': '中文摘要',
            'english_digest': '英文摘要',
            'right_object': '适用对象',
            'measure': '编写方式',
            'years': '案例年代',
            'course': '适用课程',
            'knowledge': '案例涉及理论知识',
            'time': '案例入库时间',
            'total': '查看全文',
            'explanation': '查看案例使用说明',
            'english_original': '查看微案例英文正文',
            'english_explanation': '查看微案例英文使用说明'
        })
        self.count = 0

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.writer.writerow(adapter.asdict())
        self.count += 1
        if self.count % 10 == 0:
            spider.logger.info(f"已写入 {self.count} 条案例数据")
        return item

    def close_spider(self, spider):
        self.file.close()
        spider.logger.info(f"CSV（中文表头）已关闭，共写入 {self.count} 条记录")