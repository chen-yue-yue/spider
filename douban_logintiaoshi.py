from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#慢速输入文字
def slow_input(element,input_str):
    for c in input_str:
        element.send_keys(c)
        random_delay(0.01,0.07)
    random_delay()

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
def switch_to_login_iframe():
    iframe_element =wait_element_visibility(By.XPATH,"//div[@class='login']/iframe[1]")
    driver.switch_to.frame(iframe_element)

 #切换到“密码登录”选项
def switch_to_account_login():
    switch_to_login_iframe()
    tab_account_element = wait_element_visibility(By.CLASS_NAME, "account-tab-account")
    tab_account_element.click()

## 输入用户名和密码，点击登录
def submit_username_and_password():
    username_element = wait_element_visibility(By.NAME, " ")
    password_element = wait_element_visibility(By.ID, "")
    slow_input(username_element, "username")
    slow_input(password_element, "password")
    login_btn_element = wait_element_visibility(By.CSS_SELECTOR,".btn.btn-account.btn-active")
    login_btn_element.click()

def login():
    #访问豆瓣网网页
    driver.maximize_window()
    driver.get(url)
    random_delay()
    #切换到“密码登录”选项
    switch_to_account_login()
    random_delay()
    # 输入用户名和密码，点击登录
    submit_username_and_password()
    random_delay()
    #处理滑块验证码
    driver.switch_to.frame("tcaptcha_iframe_dy")
    puzzle_piece_elements=wait_all_element_visibility(By.CLASS_NAME,"tc-fg-item")
    for puzzle_piece_element in puzzle_piece_elements:

    actions= ActionChains(driver)
    actions.click_and_hold(puzzle_piece_element).move_by_offset(50,0).release().perform()

    #判断登录是否成功

if __name__ == '__main__':
    service = Service(r"D:\SeleniumDriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver,10,0.2)
    url="https://www.douban.com/"
    login()
