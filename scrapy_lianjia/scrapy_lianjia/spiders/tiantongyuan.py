import scrapy
from scrapy_lianjia.items import ScrapyLianjiaItem

class TianTongYuanSpider(scrapy.Spider):
    name = "tiantongyuan"
    allowed_domains = ["bj.lianjia.com"]
    #start_urls = ["https://bj.lianjia.com/ershoufang/pg1/"]
    def create_page_requests(self,page):
        return scrapy.Request(
            url=f"https://bj.lianjia.com/ershoufang/pg{page}/",
            method ="GET",
            callback = self.parse,
            meta={"page":page}
        )

    def start_requests(self):
        yield self.create_page_requests(1)
    def parse(self, response):
        try:
            curr_page = response.meta['page']
            info_list = response.xpath("//div[@class='info clear']")
            self.logger.info(f"===== 开始解析第{curr_page}页，共找到{len(info_list)}条房源 =====")
            info_list=response.xpath("//div[@class='info clear']")
            print(f"[Spider] 本页找到 {len(info_list)} 个卡片")
            for info in info_list:
                #标题
                title = info.xpath("/div[@class = 'title']/a/text()").get()
                title= title.strip() if title else ""
                if not title:
                    self.logger.warning(f"房源标题解析失败：{info}")
                #标签
                clean_tags = []
                tags = info.xpath("./div[@class = 'tag']//text()").getall()
                for tag in tags:
                    stripped_tag = tag.strip()
                    if stripped_tag:
                        clean_tags.append(stripped_tag)
                tag = ",".join(clean_tags)
                if not clean_tags:
                    self.logger.warning("房源标签解析失败（无有效标签）")
                #总价
                clean_price=[]
                totalprice_list = info.xpath(".//div[@class = 'totalPrice totalPrice2']//text()").getall()
                for p in totalprice_list:
                    stripped_price = p.strip()
                    if stripped_price:
                        clean_price.append(stripped_price)
                        total_price = "".join(clean_price)
                if not clean_price:
                    self.logger.warning("房源总价解析失败")
                    total_price = "未知总价"
                #单价
                unitprice = info.xpath(".//div[@class='unitPrice']/span[1]/text()").get()
                unitprice = unitprice.strip() if unitprice else ""
                if not unitprice:
                    self.logger.warning("房源单价解析失败")
                    unitprice = "未知单价"
                #位置
                clean_position=[]
                position_list = info.xpath(".//div[@class='positionInfo']//text()").getall()
                for po in position_list:
                    stripped_position = po.strip()
                    if stripped_position:
                        clean_position.append(stripped_position)
                        position= "".join(clean_position)
                if not clean_position:
                    self.logger.warning("房源位置解析失败")
                    position = "未知位置"
                #房屋格局（几室几厅）房屋面积、朝向、装修状态、楼层、楼栋类型（板楼/塔楼等）
                details = info.xpath(".//div[@class ='houseInfo']/text()").get()
                details_list=details.split('|')
                house_range = details_list[0].strip() if len(details_list) > 0 else ""# 房屋格局
                house_area = details_list[1].strip() if len(details_list) > 1 else ""# 房屋面积
                house_toward = details_list[2].strip()  if len(details_list) > 2 else ""# 朝向
                house_situation = details_list[3].strip() if len(details_list) > 3 else "" # 装修状态
                house_floor = details_list[4].strip()  if len(details_list) > 4 else ""# 楼层
                if len(details_list)==7:
                    house_year = details_list[5].strip()  # 年份
                    house_type = details_list[6].strip()  # 楼栋类型
                else:
                    house_type = details_list[5].strip()
                    house_year ="无年份"


                # 创建Item并填充数据
                item = ScrapyLianjiaItem()
                item['title'] = title
                item['tag'] = tag
                item['total_price'] = total_price
                item['unitprice'] = unitprice
                item['position'] = position
                item['house_range'] = house_range
                item['house_area'] = house_area
                item['house_toward'] = house_toward
                item['house_situation'] = house_situation
                item['house_floor'] = house_floor
                item['house_year'] = house_year
                item['house_type'] = house_type
                # 是否近地铁
                item['is_near_subway'] = '近地铁' in clean_tags
                # 是否随时看房
                item['is_anytime']= '随时看房' in clean_tags
                # 免税类型
                tax_tag=[tag for tag in clean_tags if '房本满五年' in tag or '房本满两年' in tag ]
                item['tax_for_free'] = ','.join(tax_tag)
                yield item# 输出Item

            # 改进的分页逻辑
            try:
                # 方法1: 尝试从页码元素获取当前页码
                curr_page = response.meta.get('page')
                self.logger.info(f"当前页码(meta): {curr_page}")

                # 方法2: 尝试从页面获取当前页码
                page_on_element = response.xpath("//div[@class='page-box fr']//a[@class='on']")
                if page_on_element:
                    page_num = page_on_element.xpath("text()").get()
                    self.logger.info(f"当前页码(页面): {page_num}")
                else:
                    self.logger.warning("未找到当前页码元素")

                # 保存页面内容用于调试（仅保存前2页）
                if curr_page <= 2:
                    with open(f"page_{curr_page}_debug.html", "w", encoding="utf-8") as f:
                        f.write(response.text)
                    self.logger.info(f"页面内容已保存到 page_{curr_page}_debug.html")

                # 方法3: 尝试使用不同的XPath选择器获取下一页按钮
                # 尝试1: 原始选择器
                next_page_selector1 = "//div[@class='page-box fr']//a[contains(text(),'下一页')]"
                next_page_element1 = response.xpath(next_page_selector1)
                self.logger.info(f"尝试选择器1 - 下一页按钮数量: {len(next_page_element1)}")

                # 尝试2: 可能的新选择器（根据页面结构调整）
                next_page_selector2 = "//div[contains(@class, 'page-box')]//a[contains(text(),'下一页')]"
                next_page_element2 = response.xpath(next_page_selector2)
                self.logger.info(f"尝试选择器2 - 下一页按钮数量: {len(next_page_element2)}")

                # 尝试3: 直接根据类名查找
                next_page_selector3 = "//a[@class='next']"
                next_page_element3 = response.xpath(next_page_selector3)
                self.logger.info(f"尝试选择器3 - 下一页按钮数量: {len(next_page_element3)}")

                # 确定要使用的下一页元素
                next_page_element = None
                if next_page_element1:
                    next_page_element = next_page_element1
                    self.logger.info("使用选择器1找到下一页按钮")
                elif next_page_element2:
                    next_page_element = next_page_element2
                    self.logger.info("使用选择器2找到下一页按钮")
                elif next_page_element3:
                    next_page_element = next_page_element3
                    self.logger.info("使用选择器3找到下一页按钮")

                # 尝试简化的分页逻辑：不依赖页面元素，直接根据页码构造URL
                if curr_page < 10:
                    # 只爬取前10页进行测试
                    next_page = curr_page + 1
                    self.logger.info(f"直接构造下一页URL，页码: {next_page}")
                    yield self.create_page_requests(next_page)
                else:
                    if curr_page >= 30:
                        self.logger.info(f"已爬取到第{curr_page}页，达到30页上限，停止爬取")
                    else:
                        self.logger.info(f"已爬取到第{curr_page}页，测试完成")

                #next_page_element = response.xpath("//div[@class ='page-box fr']/div/a[contains(text(),'下一页')]")
               #if next_page_element:
                #next_page=response.meta['page']
                 #next_page = curr_page+1
                   # if next_page <= 10:
                      #  yield self.create_page_requests(next_page)


            except Exception as e:
                self.logger.error(f"分页逻辑错误: {e}", exc_info=True)
                # 保存当前页面内容用于分析
                with open(f"page_error_debug.html", "w", encoding="utf-8") as f:
                    f.write(response.text)
        except Exception as e:
            self.logger.error(f"列表页解析异常:{e}")