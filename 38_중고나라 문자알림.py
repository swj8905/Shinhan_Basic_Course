from selenium import webdriver
import time
import chromedriver_autoinstaller

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
browser.get("http://cafe.daum.net/talingpython")
time.sleep(3)
browser.switch_to.frame(browser.find_element_by_css_selector("iframe#down"))
# 중고나라 게시판 클릭
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()
time.sleep(3)

try:
    f = open("./중고나라.txt", "r", encoding="utf-8")
    ref = f.readlines()
except:
    f = open("./중고나라.txt", "w")
    ref = []

title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if (i.text+"\n") not in ref:
        f = open("./중고나라.txt", "a")
        f.write(i.text + "\n")
        f.close()
        if "냉장고" in i.text:
            new_one += 1
browser.close()
print(f"냉장고 관련 글이 {new_one}개가 올라왔습니다.")

if new_one >= 1:
    from twilio.rest import Client

    account_sid = "AC248fdb466430db7e8cd58eca08bfddde"
    auth_token = "17020dfeabe95761aab3c1a0c1455485"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"냉장고 관련 글이 {new_one}개가 올라왔습니다.  https://cafe.daum.net/talingpython/rRa6",
                         from_='+14582188747',
                         to='+821095518905'
                     )
