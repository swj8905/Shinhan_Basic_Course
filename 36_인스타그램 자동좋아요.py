from selenium import webdriver
import time
import chromedriver_autoinstaller
import random

hash_tag = input("해시태그 입력 >> ")

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://www.instagram.com/accounts/login/?hl=ko")
time.sleep(3)

id = browser.find_element_by_name("username")
id.send_keys("tutor_pyson")
pw = browser.find_element_by_name("password")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
time.sleep(4)

url = f"https://www.instagram.com/explore/tags/{hash_tag}/?hl=ko"
browser.get(url)
time.sleep(4)
# 첫번째 사진 클릭
browser.find_element_by_css_selector("div._9AhH0").click()
time.sleep(5)
# 자동 좋아요 시작.
while True:
    like = browser.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg")
    value = like.get_attribute("aria-label")
    next = browser.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow")
    if value == "좋아요":
        like.click()
        time.sleep(random.randint(30, 40) + random.random())
        next.click()
        time.sleep(random.randint(30, 40) + random.random())
    else:
        next.click()
        time.sleep(random.randint(30, 40) + random.random())






