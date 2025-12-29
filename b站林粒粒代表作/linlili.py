import requests
import datetime
url = "https://api.bilibili.com/x/space/masterpiece?vmid=523995133&web_location=333.1387"

payload = {}
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)
try:
  json_list = response.json()
  data_list = json_list["data"]
 # print(data_list)
  for data in data_list:
      #提取代表作标题
      title = data["title"] if data["title"] else "暂无标题"
      print(f"标题:{title}")
      #提取代表作包含视频数
      count = data["videos"] if data["videos"] else "0"
      print(f"包含视频数:{count}")
      #提取视频总时长
      duration = data["duration"] if data["duration"] else "0"
      duration_ = int(duration)
      h = duration_//3600
      m = (duration_%3600)//60
      s = duration_%60
      time = f"{h}小时{m}分钟{s}秒"
      print(f"视频总时长:{h}小时{m}分钟{s}秒")
      #提取发布日期
      pubdate = data["pubdate"] if data["pubdate"] else "暂无日期"
      pubdate_ = datetime.datetime.fromtimestamp(pubdate)
      print(f"发布日期:{pubdate_}")
      #提取观看次数
      view = data["stat"]["view"] if data["stat"]["view"] else "0"
      #print(f"观看次数:{view}")
      #提取弹幕条数
      danmaku = data["stat"]["danmaku"] if data["stat"]["danmaku"] else "0"
      print(f"弹幕条数:{danmaku}")
      #点赞数
      like = data["stat"]["like"] if data["stat"]["like"] else "0"
      print(f"点赞数:{like}")
      #分享次数
      share= data["stat"]["share"] if data["stat"]["share"] else "0"
      print(f"分享次数:{share}")
      #收藏数
      favorite=data["stat"]["favorite"] if data["stat"]["favorite"] else "0"
      print(f"收藏数:{favorite}")
      print("\n")
      master_pieces={"标题":title,
                     "包含视频数":count,
                     "视频总时长":time,
                     "发布日期":pubdate_,
                     "观看次数":view,
                     "弹幕条数":danmaku,
                     "点赞数":like,
                     "分享次数":share,
                     "收藏数":favorite
                     }
      for key,value in master_pieces.items():
        print(f"{key}:{value}")


except Exception as e:
  print(e)