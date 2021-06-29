from selenium import webdriver
import time
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://www.youtube.com/watch?v=95ULYjyiFLQ")
time.sleep(4)
# 스크롤 내리기
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN) # PAGE_DOWN : 스크롤 살짝 / END : 스크롤 끝까지
time.sleep(4)
comments = browser.find_elements_by_css_selector("#content-text")
idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("크롤링 끝!")
        break
    idx += 1
    if idx % 15 == 0:
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(3)
        comments = browser.find_elements_by_css_selector("#content-text")