import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

#随机延迟
def random_delay(min_delay=1.0,max_delay =2.0):
    time.sleep(random.uniform(min_delay,max_delay))

#切换新标签页
def shift_new_page(page):
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == page)
    driver.switch_to.window(driver.window_handles[-1])

#查找并点击搜索框,输入林粒粒
def show_search_box(keys):
    search_box = driver.find_element(By.CLASS_NAME,"nav-search-input")
    search_box.clear()
    search_box.click()
    search_box.send_keys(keys)
    random_delay()
 #点击搜索
def press_search_button():
    search_button = driver.find_element(By.CLASS_NAME,"nav-search-btn")
    search_button.click()
    random_delay()

# 点击进入林粒粒主页
def run_into_pointer():
    pointer = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'user-name cs_pointer v_align_middle')]")))
    time.sleep(0.5)
    pointer.click()
    random_delay()

# 解析代表作列表
def masterpiece_list():
    master_pieces_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"masterpiece-block")))
    masterpieces_list = master_pieces_list.find_elements(By.CLASS_NAME,"bili-video-card__wrap")
    for masterpiece in masterpieces_list:
    #解析标题,播放次数，弹幕数，视频总时长
        parse_video_details(masterpiece)
    random_delay()


#获取代表作个数
def get_masterpiece_num():
    master_pieces_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"masterpiece-block")))
    masterpieces_list = master_pieces_list.find_elements(By.CLASS_NAME,"bili-video-card__wrap")
    masterpiece_num = len(masterpieces_list)
    return masterpiece_num

#定位标题,播放次数，弹幕数，视频总时长
def parse_video_details(masterpiece):
    video_title_element=masterpiece.find_element(By.CLASS_NAME,"bili-video-card__title")
    #video_title = video_title_element.find_element(By.XPATH,"a").text
    video_title = video_title_element.get_attribute("title")
    video_detail_elements = masterpiece.find_elements(By.CLASS_NAME,"bili-cover-card__stat")
    video_playdata = video_detail_elements[0].find_element(By.XPATH,"span").text
    video_danmu = video_detail_elements[1].find_element(By.XPATH,"span").text
    video_duration  = video_detail_elements[2].find_element(By.XPATH,"span").text
    print(f"标题:{video_title}")
    print(f"播放次数:{video_playdata}")
    print(f"弹幕数:{video_danmu}")
    print(f"视频总时长:{video_duration}")
    print("\n")

def get_bili_masterpiece(name):
    try:
        # 查找并点击搜索框,输入林粒粒
        show_search_box(name)
        # 点击搜索,等跳转（新增）
        press_search_button()
        #print("当前标签页句柄：", driver.current_window_handle)
        #print("当前标签页数量：", len(driver.window_handles))
        shift_new_page(2)
        # 点击进入林粒粒主页
        run_into_pointer()
        shift_new_page(3)
        # 解析代表作信息
        masterpiece_list()
        masterpiece_num = get_masterpiece_num()
        print(f"共有{masterpiece_num}个代表作")
    except Exception as e:
        print(e)
        traceback.print_exc()

if __name__ =='__main__':
    service = Service(r"D:\SeleniumDriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.bilibili.com/")
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.2)
    random_delay()
    get_bili_masterpiece("宋浩")