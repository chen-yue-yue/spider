import re
from bs4 import BeautifulSoup
import requests
from lxml import etree


headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"}
response = requests.get("https://book.douban.com/subject/6518605/",headers=headers)
html = response.text
soup =BeautifulSoup(html,"html.parser")
#获取书名
all_titles = soup.findAll("span",attrs={"property":"v:itemreviewed"})
for title in all_titles:
    print(f"书名:{title.string}")
info = soup.find('div',attrs = {'id':'info'})
#获取作者
author = info.find_all('span')[0].find('a')
print(f"作者:{author.string}")
#获取出版社
publishing_house = info.findALL.findAll("a")[0]
print(f"出版社:{publishing_house.string}")
#获取出品方
publisher = info.findAll("a")[1]
print(f"出品方:{publisher.string}")
#获取副标题
subtitle= info.findAll("span")[3]
print(f"{subtitle.string}")
#用xpath提取出版日期，页数，定价，豆瓣评分，评价人数，短评数量
tree = etree.HTML(html)
info_list = tree.xpath("//div[@id='info']")
year_list = info_list.xpath(".//span[5]/text()")
year = year_list[0] if year_list else None
print(f"{year}")

page_list = info.xpath(".//span[6]/text()")
page = page_list[0] if page_list else  None
print(f"{page}")

price_list = info.xpath(".//span[6]/text()")
price=price_list[0] if page_list else None
print(f"{price}")

score_list = tree.xpath("//div[@class= 'll rating_num']/text()")
score = score_list[0] if score_list else None
print(f"豆瓣评分:{score}")

rating_num_list=tree.xpath("//span[@class='rating_num']/text()")
rating_num =rating_num_list[0] if rating_num_list else None
print(f"评价人数:{rating_num}")

comments_num_list = tree.xpath("//div[@class='mod-hd']/text()")
comments_num_text = comments_num_list[0].strip() if comments_num_list else None
comments_num_match = re.search(r" \d+",comments_num_text)
comments_num=comments_num_match.group() if comments_num_match else None
print(f"短评数量:{comments_num}")

