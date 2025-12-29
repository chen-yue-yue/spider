
import requests
from lxml import etree


headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0" }
url="https://movie.douban.com/top250"
try:
    for start in range(0,250,25):
        page_url =f"{url}?start={start}"
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()

        html = response.text
        tree = etree.HTML(html)
        #获取class为item的列表
        item_list = tree.xpath("//div[@class='item']")
        for item in item_list:
            #获取标题
            title_list =item.xpath(".//div[@class ='hd']/a/span[1]/text()")
            title = title_list[0] if title_list else None
            #获取评分
            score_list = item.xpath(".//span[@class='rating_num']/text()")
            score = score_list[0] if score_list else None
            print (f"标题:{title}.评分:{score}")

except requests.RequestException as e:
    print(f"请求失败：{e}")
except Exception as e:
    print(f"发生错误：{e}")