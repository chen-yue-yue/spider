import scrapy
import asyncio
import csv
import os



class XhsCommentSpider(scrapy.Spider):
    name = "xhs_comment"
    allowed_domains = ["xiaohongshu.com"]
    start_urls = ["https://www.xiaohongshu.com/explore"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_context": "default",
                    'playwright_page_goto_kwargs': {
                        'wait_until': 'networkidle',
                    }
                },
                callback=self.parse,
            )
    
    async def fill_search_box(self,page,keys):
        search_box_selector = "//div[@class='input-box']/input"
        try:
            await page.wait_for_selector(search_box_selector, timeout=5000)
            await page.fill(search_box_selector, keys)
            self.logger.info(f"搜索框填充成功，关键词：{keys}")
        except Exception as e:
            self.logger.error(f"搜索框操作失败：{str(e)}")
            raise

    async def scroll_until_the_end(self, page, timeout=300000, step_delay=0.5, max_scrolls=500):
        self.logger.info("开始执行真人模拟滚动...")
        last_height = await page.evaluate("document.body.scrollHeight")
        no_change_count = 0
        loaded_note_count = 0

        for i in range(max_scrolls):
            await page.mouse.wheel(0, 1000)

            await asyncio.sleep(0.2)

            if i % 10 == 0:
                current_note_count = await page.evaluate("""() => {
                    return document.querySelectorAll('section.note-item').length;
                }""")
                self.logger.info(f"第{i}次滚动 | 已加载帖子数：{current_note_count}")

                the_end = await page.query_selector("xpath=//*[contains(text(),'THE END')]|//*[contains(text(),'没有更多了')]")
                if the_end:
                    self.logger.info("找到THE END/没有更多了，停止滚动")
                    break

                new_height = await page.evaluate("document.body.scrollHeight")
                if current_note_count == loaded_note_count and new_height == last_height:
                    no_change_count += 1
                else:
                    no_change_count = 0
                    loaded_note_count = current_note_count
                    last_height = new_height

                if no_change_count >= 10:
                    self.logger.info("疑似到底，强制加载最后内容...")
                    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    await asyncio.sleep(3)
                    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    await asyncio.sleep(2)
                    final_count = await page.evaluate("document.querySelectorAll('section.note-item').length")
                    self.logger.info(f"最终加载的帖子数：{final_count}")
                    break

            if i % 50 == 0:
                self.logger.info(f">>> 累计滚动 {i} 次 | 已加载帖子数：{loaded_note_count}")

        self.logger.info("滚动任务结束，最终页面高度：%s", last_height)

    
    async def create_note_requests(self, note_url):
        return scrapy.Request(
            url=note_url,
            method="GET",
            callback=self.parse_note,
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        all_note_urls = set()

        try:
            await self.fill_search_box(page, "电影")
            await page.click("//div[@class='input-box']/div")
            
            await page.wait_for_selector("section.note-item", timeout=15000)
            self.logger.info("检测到结果流入，开始自动滚动提取...")
            self.logger.info("程序将自动向下滚动并提取链接...")
            
            await asyncio.sleep(2)
            
            last_loaded_count = 0
            no_new_content_count = 0
            last_url_count = 0
            
            for i in range(500):
                await page.evaluate("window.scrollBy(0, 1000)")
                await asyncio.sleep(0.25)
                
                current_note_count = await page.evaluate('''() => {
                    return document.querySelectorAll('section.note-item').length;
                }''')
                
                current_urls = await page.evaluate('''() => {
                    const result = [];
                    const items = document.querySelectorAll('section.note-item');
                    items.forEach(item => {
                        const links = item.querySelectorAll('a');
                        for (let a of links) {
                            const href = a.getAttribute('href');
                            if (href && href.includes('explore/')) {
                                result.push('https://www.xiaohongshu.com' + href);
                                break;
                            }
                        }
                    });
                    return result;
                }''')
                
                new_urls_count = 0
                for url in current_urls:
                    if url not in all_note_urls:
                        all_note_urls.add(url)
                        new_urls_count += 1
                
                if i % 10 == 0 or new_urls_count > 0:
                    self.logger.info(f"第 {i} 次滚动 | 新增 {new_urls_count} 条 | 累计 {len(all_note_urls)} 条 | 页面帖子: {current_note_count}")
                
                end_container = await page.query_selector("xpath=//div[contains(@class,'end-container')]")
                if end_container:
                    self.logger.info("检测到THE END标志，完成提取")
                    break
                
                if current_note_count == last_loaded_count and len(all_note_urls) == last_url_count:
                    no_new_content_count += 1
                else:
                    no_new_content_count = 0
                    last_loaded_count = current_note_count
                    last_url_count = len(all_note_urls)
                
                if no_new_content_count >= 5:
                    self.logger.info("页面无新内容加载，已到底")
                    break
                
                if i % 50 == 0:
                    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    await asyncio.sleep(0.5)

            self.logger.info(f"======= 提取完成：共 {len(all_note_urls)} 条去重链接 =======")
            
            for i, url in enumerate(list(all_note_urls)[:5]):
                self.logger.info(f"链接 {i+1}: {url}")
            
            csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'xhs_note_urls.csv')
            csv_file_path = os.path.normpath(csv_file_path)
            
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['序号', '帖子链接'])
                for idx, url in enumerate(all_note_urls, 1):
                    writer.writerow([idx, url])
            
            self.logger.info(f"链接已保存到: {csv_file_path}")

        except Exception as e:
            self.logger.error(f"解析异常：{e}")
        finally:
            try:
                await page.close()
            except:
                pass
            
    async def parse_note(self, response):
        pass
