
import requests
from lxml import etree
import re

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
    }
url="https://movie.douban.com/top250"
try:
    for start in range(0,250,25):
        page_url =f"{url}?start={start}"
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()

        html = response.text
        tree = etree.HTML(html)
        #获取class为item的列表
        item_list = tree.xpath(".//div[@class='item']")
        for item in item_list:
            #获取标题
            title_list =item.xpath(".//div[@class ='hd']/a/span[1]/text()")
            title = title_list[0] if title_list else None
            #获取评分
            score_list = item.xpath(".//span[@class='rating_num']/text()")
            score = score_list[0] if score_list else None

            #获取排名
            rank_element=item.xpath(".//div[@class = 'pic']/em/text()")
            rank=rank_element[0] if rank_element else None

            #获取评价人数
            rating_num = item.xpath(".//div[@class='bd']/div/span[4]")
            rating_num_html = etree.tostring(rating_num[0],encoding='unicode').strip() if rating_num else None
            rating_num_match= re.search(r"\d+",rating_num_html)
            num =rating_num_match.group() if rating_num_match else None
            print(f"标题:{title}.评分:{score}.排名:{rank}.评价人数:{num}")
            #获取导演
            director_element = item.xpath(".//div[@class='bd']/p[1]/text()")
            director_text = director_element[0].strip() if director_element else None
            director_match = re.search(r"导演[:：]\s*(.*?)((\s{2,}主)|(\.{3}))",director_text)
            director_text=director_match.group(1)
            director_list= director_text.split(" / ")
            for director in director_list:
                print(f"导演:{director}")
            #获取年份
            year_text = director_element[1].strip() if director_element else None
            year_match =re.search(r"\d+",year_text)
            year = year_match.group() if year_match else None
            print(f"年份:{year}")
except requests.RequestException as e:
    print(f"请求失败：{e}")
except Exception as e:
    print(f"发生错误：{e}")