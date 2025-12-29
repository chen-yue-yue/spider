import requests
import datetime
import traceback

#提取代表作标题
def get_title(data_):
    # get方法：第一个参数是键，第二个是默认值
    title_ = data_.get("title", "暂无标题")
    return title_.strip()
#提取代表作包含视频数
def get_count(data_):
    count_ = data_.get("videos", 0)
    return int(count_)

#提取视频总时长
def get_duration(data_):
    duration_ = data_.get("duration", 0)
    duration_total = int(duration_)
    h = duration_total // 3600
    m = (duration_total % 3600) // 60
    s = duration_total % 60
    time_ = f"{h}小时{m}分钟{s}秒"
    return time_

#提取发布日期
def get_pubdate(data_):
    date = data_.get("pubdate", 0)
    pubdate_ = datetime.datetime.fromtimestamp(date)
    return pubdate_

#提取观看次数
def get_view(data_):
    # 第一步：取stat，默认空字典；第二步：取view，默认0
    stat = data_.get("stat", {})
    view_ = stat.get("view", 0)
    return int(view_)

#提取弹幕条数
def get_danmaku(data_):
    stat = data_.get("stat", {})
    danmaku_ = stat.get("danmaku", 0)
    return int(danmaku_)

#提取点赞数
def get_like(data_):
    stat = data_.get("stat", {})
    like_ = stat.get("like", 0)
    return int(like_)

#提取分享次数
def get_share(data_):
    stat = data_.get("stat", {})
    share_ = stat.get("share", 0)
    return int(share_)

#提取收藏数
def get_favorite(data_):
    stat = data_.get("stat", {})
    favorite_ = stat.get("favorite", 0)
    return int(favorite_)

#创建代表作字典
def create_masterpiece_dict(title_,count_,time_,pubdate_,view_,danmaku_,like_,share_,favorite_):
    master_pieces = {"标题": title_,
                     "包含视频数": count_,
                     "视频总时长": time_,
                     "发布日期": pubdate_,
                     "观看次数": view_,
                     "弹幕条数": danmaku_,
                     "点赞数": like_,
                     "分享次数": share_,
                     "收藏数": favorite_
                     }
    return master_pieces

#爬取代表作数据
def scrape_masterpiece(vmid):
    try:
        #请求代表作API
        url = f"https://api.bilibili.com/x/space/masterpiece?vmid={vmid}&web_location=333.1387"
        payload = {}
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
        #获取代表作列表
        json_list = response.json()
        data_list = json_list["data"]
        #循环代表作列表，获取各个数据
        for data in data_list:
            # 提取代表作标题
            title = get_title(data)
            # 提取代表作包含视频数
            count = get_count(data)
            # 提取视频总时长
            time = get_duration(data)
            # 提取发布日期
            pubdate_ = get_pubdate(data)
            # 提取观看次数
            view = get_view(data)
            # 提取弹幕条数
            danmaku = get_danmaku(data)
            # 点赞数
            like = get_like(data)
            # 分享次数
            share = get_share(data)
            # 收藏数
            favorite = get_favorite(data)
            # 创建代表作字典
            master_pieces = create_masterpiece_dict(title, count, time, pubdate_, view, danmaku, like, share, favorite)
            for key, value in master_pieces.items():
                print(f"{key}:{value}")
            print()
    except Exception as e:
        print(e)
        traceback.print_exc()

if __name__ =='__main__':
    scrape_masterpiece(523995133)