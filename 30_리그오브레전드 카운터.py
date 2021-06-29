from selenium import webdriver
import time
import chromedriver_autoinstaller

your_champ = input("상대방이 고른 챔프 입력 >> ")
chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://www.op.gg/champion/statistics")
# your_champ 클릭하게 만들기
champs = browser.find_elements_by_css_selector("div.champion-index__champion-item__name")
for i in champs:
    if i.text == your_champ:
        i.click()
        break
time.sleep(3)
# 카운터 메뉴 클릭
menu = browser.find_element_by_css_selector("li.champion-stats-menu__list__item.champion-stats-menu__list__item--red.tabHeader > a")
menu.click()
time.sleep(2)
# 카운터 챔프 크롤링
counter_champ = browser.find_elements_by_css_selector("div.champion-matchup-list__champion > span:nth-child(2)")
for i in counter_champ:
    print(i.text)
browser.close()



# 카운터 챔프 크롤링