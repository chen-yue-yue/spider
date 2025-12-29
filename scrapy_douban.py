import requests
from bs4 import BeautifulSoup
for start in range(0,250,25):
    url=f"https://movie.douban.com/top250?start={start}"
    headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"}
    response = requests.get(url,headers = headers)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    all_titles=soup.findAll("span",attrs={"class":"title"})
    for title in all_titles:
       title_string =title.string
       if "/" not in title_string:
          print(title_string)