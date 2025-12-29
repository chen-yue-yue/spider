import re
from bs4 import BeautifulSoup
import requests
from lxml import etree


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
    }
url = "https://book.douban.com/subject/6518605/"

try:
       response = requests.get(url, headers=headers)
       response.raise_for_status()  # 检查请求是否成功
       html = response.text
       soup = BeautifulSoup(html, "html.parser")
       tree = etree.HTML(html)

        # 获取书名
       title_tag = soup.find("span", attrs={"property": "v:itemreviewed"})
       title = title_tag.string.strip() if title_tag else "未知书名"
       #print("书名标签是否存在？", title_tag is not None)
       print(f"书名: {title}")
       info = soup.find("div", attrs={"id": "info"})
       if not info:
               print("未能找到 'info' 区块，可能是反爬机制导致页面内容异常。")
       # 获取作者
       else:
               author = info.find_all("span")[0].find("a")
               print(f"作者: {author.string}")
        # 获取出版社
               publishing_house = info.find_all("a")[1]
               print(f"出版社: {publishing_house.string}")
               # 获取出品方
               publisher = info.find_all("a")[2]
               print(f"出品方: {publisher.string}")
               # 获取副标题
               subtitle_tag = info.find_all("span")[4].find_next_sibling(string=True)
               subtitle = subtitle_tag.strip() if subtitle_tag else "无副标题"
               print(f"副标题: {subtitle}")
               # 用xpath提取出版日期，页数，定价，豆瓣评分，评价人数，短评数量
               info_list = tree.xpath("//div[@id='info']")
               for info in info_list:
                   year_list = info.xpath(".//span[contains(text(), '出版年')]/following-sibling::text()[1]")
                   year = year_list[0].strip() if year_list else "未知出版年"
                   print(f"年份: {year}")

                   page_list = info.xpath(".//span[contains(text(),'页数')]/following-sibling::text()[1]")
                   page = page_list[0].strip() if page_list else "未知页数"
                   print(f"页数: {page}")

                   price_list = info.xpath(".//span[contains(text(),'定价')]/following-sibling::text()[1]")
                   price = price_list[0].strip() if price_list else "未知定价"
                   print(f"价格: {price}")

               score_list = tree.xpath("//strong[@class= 'll rating_num 'and @property='v:average']/text()")
               score = score_list[0].strip() if score_list else "暂无评分"
               print(f"豆瓣评分: {score}")

               rating_num_list = tree.xpath(
                   "//a[@href='comments' and @class='rating_people']/span/text()")  # //strong[contains(@class, 'rating_num') and @property='v:average']/text()")
               rating_num = rating_num_list[0] if rating_num_list else "暂无评价"
               print(f"评价人数: {rating_num}")

               comments_num_list = tree.xpath("//div[@class='mod-hd']/h2/span[@class='pl']/a/text()")
               comments_num_text = comments_num_list[0].strip() if comments_num_list else None
               comments_num_match = re.search(r" \d+", comments_num_text)
               comments_num = comments_num_match.group().strip() if comments_num_match else "暂无短评"
               print(f"短评数量: {comments_num}")


except requests.RequestException as e:
        print(f"请求失败：{e}")
except Exception as e:
        print(f"发生其他错误：{e}")

