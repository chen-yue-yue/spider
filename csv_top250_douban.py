
import requests
from lxml import etree
import re
import csv



headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
    }
url="https://movie.douban.com/top250"


def write_movies_to_csv(movies_):
    with open('douban_top250_movies.csv', 'w',newline ='', encoding='utf-8-sig') as f:
         fieldnames=["排名","标题","评分","年份","评价人数","导演"]
         writer=csv.DictWriter(f,fieldnames =fieldnames)
         writer.writeheader()
         writer.writerows(movies_)
    print("电影信息已写入 douban_top250_movies.csv")

#获取标题
def get_title(item_):
    title_list = item_.xpath(".//div[@class ='hd']/a/span[1]/text()")
    title_ = title_list[0] if title_list else None
    return title_

#获取评分
def get_score(item_):
    score_list = item_.xpath(".//span[@class='rating_num']/text()")
    score_ = score_list[0] if score_list else None
    return  score_

#获取排名
def get_rank(item_):
    rank_element = item_.xpath(".//div[@class = 'pic']/em/text()")
    rank_ = rank_element[0] if rank_element else None
    return rank_

#获取评价人数
def get_rating_num(item_):
    rating_num = item_.xpath(".//div[@class='bd']/div/span[4]")
    rating_num_html = etree.tostring(rating_num[0], encoding='unicode').strip() if rating_num else None
    rating_num_match = re.search(r"\d+", rating_num_html)
    num_ = rating_num_match.group() if rating_num_match else None
   # print(f"标题:{title}.评分:{score}.排名:{rank}.评价人数:{num}")
    return  num_

#获取导演
def get_director(item_):
    director_element = item_.xpath(".//div[@class='bd']/p[1]/text()")
    director_text = director_element[0].strip() if director_element else None
    director_match = re.search(r"导演[:：]\s*(.*?)((\s{2,}主)|(\.{3}))", director_text)
    director_text = director_match.group(1)
    director_list_ = director_text.split(" / ")
    return  director_list_

#获取年份
def get_year(item_):
    year_text = item_.xpath(".//div[@class = bd]/p[1]/text()")[1]
    year_match = re.search(r"\d+", year_text)
    year_ = year_match.group() if year_match else None
    #print(f"年份:{year}")
    return year_

#创建电影信息字典
def create_movie_dict(rank_,title_,score_,num_,year_,director_list_):
    movie_dict_ = {
        "标题": title_,
        "评分": score_,
        "排名": rank_,
        "评价人数": num_,
        "年份": year_,
        "导演": ",".join(director_list_)
    }
    return movie_dict_

def scrape_top250_movies():
    try:
        movies = []
        for start in range(0, 250, 25):
            page_url = f"{url}?start={start}"
            response = requests.get(page_url, headers=headers)
            response.raise_for_status()

            html = response.text
            tree = etree.HTML(html)
            # 获取class为item的列表
            item_list = tree.xpath("//div[@class='item']")
            for item in item_list:
                # 获取标题
                title = get_title(item)
                # 获取评分
                score = get_score(item)
                # 获取排名
                rank = get_rank(item)
                # 获取评价人数
                num = get_rating_num(item)
                # 获取导演
                director_list = get_director(item)
                # 获取年份
                year = get_year(item)

                # 创建电影信息字典
                movie_dict = create_movie_dict(rank, title, score, num, year, director_list)
                movies.append(movie_dict)
        write_movies_to_csv(movies)
    except requests.RequestException as e:
        print(f"请求失败：{e}")
    except Exception as e:
        print(f"发生错误：{e}")

if __name__=='__main__':
    scrape_top250_movies()