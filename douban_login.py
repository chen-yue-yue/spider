from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#随机暂停模拟人类操作
def random_delay(min_delay=1.0,max_delay=3.0):
    time.sleep(random.uniform(min_delay,max_delay))

#显示等待单个元素可见
def wait_element_visibility(locator_type,locator_value):
    element = wait.until(EC.visibility_of_element_located((locator_type,locator_value)))
    return element

#显示等待多个元素可见
def wait_all_element_visibility(locator_type,locator_value):
    elements = wait.until(EC.visibility_of_all_elements_located((locator_type,locator_value)))
    return elements

#切换到登录模块所在的iframe
def switch_to_iframe():
    iframe_element =wait_element_visibility(By.XPATH,"//div[@class='login']/iframe[1]")
    driver.switch_to.frame(iframe_element)


def login():
    #访问豆瓣网网页
    driver.maximize_window()
    driver.get(url)
    random_delay()
    #切换到“密码登录”选项
    iframe_element = driver.find_element(By.XPATH, "//div[@class='login']/iframe[1]")
    driver.switch_to.frame(iframe_element)
    tab_account_element = driver.find_element(By.CLASS_NAME,"account-tab-account")
    tab_account_element.click()
    username_element = driver.find_element(By.NAME,"username")
    password_element = driver.find_element(By.ID, "password")
    #输入用户名和密码，点击登录
    username_element.send_keys("13643078487")
    password_element.send_keys("qazwsxedc147.")
    password_element.send_keys(Keys.ENTER)
    random_delay()
    #处理滑块验证码
    driver.switch_to.frame("tcaptcha_iframe_dy")
    puzzle_piece_element=driver.find_element(By.CLASS_NAME,"tc-fg-item")
    actions= ActionChains(driver)
    actions.click_and_hold(puzzle_piece_element).move_by_offset(50,0).release().perform()

    #判断登录是否成功

if __name__ == '__main__':
    service = Service(r"D:\SeleniumDriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver,10,0.2)
    url="https://www.douban.com/"
    login()