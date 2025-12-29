import scrapy
from scrapy_cmcc.items import ScrapyCmccItem

class CmccDlutSpider(scrapy.Spider):
    name = "cmcc_dlut"
    allowed_domains = ["cmcc-dlut.cn"]

    def create_page_requests(self,page):
        return scrapy.Request(
            url=f"http://www.cmcc-dlut.cn/Cases/Latest/{page}",
            method ="GET",
            callback = self.parse,
            meta={"page":page}
        )

    def create_case_requests(self, case_url):
        return scrapy.Request(
            url=f"http://www.cmcc-dlut.cn{case_url}",
            method="GET",
            callback=self.parse_case,
        )

    def start_requests(self):
        yield self.create_page_requests(1)

    def parse(self, response):
        page = response.meta['page']
        self.logger.info(f"当前请求第{page}页")
        try:
            # 尝试提取所有案例URL
            case_urls = response.xpath("//td[@class='a_left']/a/@href").getall()
            
            # 去除重复的URL
            unique_case_urls = list(set(case_urls))
            self.logger.info(f"第{page}页提取到{len(unique_case_urls)}个案例URL")
            
            # 处理当前页的案例URL
            for case_url in unique_case_urls:
                yield self.create_case_requests(case_url)
            
            # 分页逻辑 - 根据用户要求总共有10228个案例，每页18个，共569页
            curr_page = response.meta['page']
            next_page = curr_page + 1
            
            if next_page <= 569:
                self.logger.info(f"准备爬取下一页: {next_page}")
                yield self.create_page_requests(next_page)
            else:
                self.logger.info(f"已爬取到最后一页569页，停止分页爬取")

        except Exception as e:
            self.logger.error(f"列表页解析异常: {e}", exc_info=True)

    def parse_case(self,response):
        try:
            # 获取案例信息
            info_table = response.xpath("//table[@class='infotable']/tbody")
            # 案例编号
            case_id = info_table.xpath("./tr[2]/td/text()").get()
            case_id = case_id.strip() if case_id else ""
            if not case_id:
                self.logger.warning("案例编号解析失败")
            # 被浏览次数
            num = info_table.xpath("./tr[3]/td/text()").get()
            num = num.strip() if num else ""
            if not num:
                self.logger.warning("被浏览次数解析失败")
            # 案例名称
            case_title = info_table.xpath("./tr[4]/td/text()").get()
            case_title= case_title.strip() if case_title else ""
            if not case_title:
                self.logger.warning("案例名称解析失败")
            # 译名
            translate_name = info_table.xpath("./tr[5]/td/text()").get()
            translate_name = translate_name.strip() if translate_name else ""
            if not translate_name:
                self.logger.warning("译名解析失败")
            # 案例作者
            writer = info_table.xpath("./tr[6]/td/text()").get()
            writer = writer.strip() if writer else ""
            if not writer:
                self.logger.warning("案例作者解析失败")
            # 作者单位
            workplace = info_table.xpath("./tr[7]/td/text()").get()
            workplace = workplace.strip() if workplace else ""
            if not workplace:
                self.logger.warning("作者单位解析失败")
            # 指导者
            director = info_table.xpath("./tr[8]/td/text()").get()
            director = director.strip() if director else ""
            if not director:
                self.logger.warning("指导者解析失败")
            # 译者
            translate_worker = info_table.xpath("./tr[9]/td/text()").get()
            translate_worker = translate_worker.strip() if translate_worker else ""
            if not translate_worker:
                self.logger.warning("译者解析失败")
            # 案例企业名称
            company = info_table.xpath("./tr[10]/td/text()").get()
            company = company.strip() if company else ""
            if not company:
                self.logger.warning("案例企业名称解析失败")
            # 行业
            industry = info_table.xpath("./tr[11]/td/text()").get()
            industry = industry.strip() if industry else ""
            if not industry:
                self.logger.warning("行业解析失败")
            # 规模
            large = info_table.xpath("./tr[12]/td/text()").get()
            large = large.strip() if large else ""
            if not large:
                self.logger.warning("规模解析失败")
            # 案例涉及的职能领域
            area = info_table.xpath("./tr[13]/td/text()").get()
            area = area.strip() if area else ""
            if not area:
                self.logger.warning("案例涉及的职能领域解析失败")
            # 案例语种
            language = info_table.xpath("./tr[14]/td/text()").get()
            language = language.strip() if language else ""
            if not language:
                self.logger.warning("案例语种解析失败")
            # 案例正文页数
            work_page = info_table.xpath("./tr[15]/td/text()").get()
            work_page = work_page.strip() if work_page else ""
            if not work_page:
                self.logger.warning("案例正文页数解析失败")
            # 案例类型
            case_type = info_table.xpath("./tr[16]/td/text()").get()
            case_type = case_type.strip() if case_type else ""
            if not case_type:
                self.logger.warning("案例类型解析失败")
            # 中文关键字
            chinese_keywords = info_table.xpath("./tr[17]/td/text()").get()
            chinese_keywords = chinese_keywords.strip() if chinese_keywords else ""
            if not chinese_keywords:
                self.logger.warning("中文关键字解析失败")
            # 英文关键字
            english_keywords = info_table.xpath("./tr[18]/td/text()").get()
            english_keywords = english_keywords.strip() if english_keywords else ""
            if not english_keywords:
                self.logger.warning("英文关键字解析失败")
            # 中文摘要
            chinese_digest = info_table.xpath("./tr[19]/td/text()").get()
            chinese_digest = chinese_digest.strip() if chinese_digest else ""
            if not chinese_digest:
                self.logger.warning("中文摘要解析失败")
            # 英文摘要
            english_digest = info_table.xpath("./tr[20]/td/text()").get()
            english_digest = english_digest.strip() if english_digest else ""
            if not english_digest:
                self.logger.warning("英文摘要解析失败")
            # 适用对象
            right_object = info_table.xpath("./tr[21]/td/text()").get()
            right_object = right_object.strip() if right_object else ""
            if not right_object:
                self.logger.warning("适用对象解析失败")
            # 编写方式
            measure = info_table.xpath("./tr[22]/td/text()").get()
            measure = measure.strip() if measure else ""
            if not measure:
                self.logger.warning("编写方式解析失败")
            # 案例年代
            years = info_table.xpath("./tr[23]/td/text()").get()
            years = years.strip() if years else ""
            if not years:
                self.logger.warning("案例年代解析失败")
            # 适用课程
            course = info_table.xpath("./tr[24]/td/text()").get()
            course = course.strip() if course else ""
            if not course:
                self.logger.warning("适用课程解析失败")
            # 案例涉及理论知识
            knowledge = info_table.xpath("./tr[25]/td/text()").get()
            knowledge = knowledge.strip() if knowledge else ""
            if not knowledge:
                self.logger.warning("案例涉及理论知识解析失败")
            # 案例入库时间
            time = info_table.xpath("./tr[26]/td/text()").get()
            time = time.strip() if time else ""
            if not time:
                self.logger.warning("案例入库时间解析失败")
            # 查看全文
            total = info_table.xpath("./tr[27]/td/a/@href").get()
            total = "http://www.cmcc-dlut.cn/"+total.strip() if total else ""
            if not total:
                self.logger.warning("查看全文链接解析失败")
            # 查看案例使用说明
            explanation = info_table.xpath("./tr[28]/td/a/@href").get()
            explanation = "http://www.cmcc-dlut.cn/"+explanation.strip() if explanation else ""
            if not explanation:
                self.logger.warning("查看案例使用说明链接解析失败")
            # 查看微案例英文正文
            english_original = info_table.xpath("./tr[29]/td/a/@href").get()
            english_original = "http://www.cmcc-dlut.cn/"+english_original.strip() if english_original else ""
            if not english_original:
                self.logger.warning("查看微案例英文正文链接解析失败")
            # 查看微案例英文使用说明
            english_explanation = info_table.xpath("./tr[30]/td/a/@href").get()
            english_explanation = "http://www.cmcc-dlut.cn/"+english_explanation.strip() if english_explanation else ""
            if not english_explanation:
                self.logger.warning("查看微案例英文使用说明链接解析失败")
            # 创建Item并填充数据
            item = ScrapyCmccItem()
            item['case_id']=case_id
            item['num'] = num
            item['case_title'] = case_title
            item['translate_name']=translate_name
            item['writer']=writer
            item['workplace']=workplace
            item['director'] = director
            item['translate_worker']= translate_worker
            item['company']=company
            item['industry'] = industry
            item['large']=large
            item['area'] = area
            item['language']=language
            item['work_page']=work_page
            item['case_type']=case_type
            item['chinese_keywords']=chinese_keywords
            item['english_keywords']=english_keywords
            item['chinese_digest'] = chinese_digest
            item['english_digest']=english_digest
            item['right_object']=right_object
            item['measure']=measure
            item['years']=years
            item['course']=course
            item['knowledge']=knowledge
            item['time']=time
            item['total']=total
            item['explanation']=explanation
            item['english_original']=english_original
            item['english_explanation']=english_explanation
            yield item
        except Exception as e:
            self.logger.error(f"案例解析异常:{e}")
