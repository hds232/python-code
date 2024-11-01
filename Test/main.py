import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def create_driver():
    url = 'https://dxpx.uestc.edu.cn/'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver

def find_unfinished_lesson(driver):
    lessons = driver.find_elements(By.XPATH, '//div[@class="fleft"]')
    # 遍历所有课程大纲
    for lesson in lessons:
        if not lesson.find_elements(By.XPATH, './/div[contains(@style, "color:red")]'):
            continue
        else:
            return lesson.find_element(By.XPATH, './/a[@class="study_a"]')
    return None

def start():
    driver = create_driver()
    # 输入用户名和密码
    while True:
        ch = input('是否已经完成登录？(y/n/exit)')
        match ch:
            case 'y':
                break
            case 'n':
                driver.refresh()
            case 'exit':
                sys.exit()
            case _:
                print('输入错误，请重新输入！')
    # actions = ActionChains(driver)
    # 进入课程页面寻找课程大纲
    driver.find_element(By.XPATH, '//a[@href="/user/lesson"]').click()
    lessons_url = driver.current_url
    # 循环播放
    while lesson := find_unfinished_lesson(driver):
        lesson.click()
        video_list = driver.find_elements(By.XPATH, '//div[@class="video_lists"]//li[@class]//a')
        print(len(video_list))
        break
    
    # 销毁driver
    driver.quit()

if __name__ == '__main__':
    start()
    