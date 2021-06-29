from selenium import webdriver
import time
import chromedriver_autoinstaller

chrome_path = chromedriver_autoinstaller.install()
opt = webdriver.ChromeOptions()
opt.add_argument("headless")
browser = webdriver.Chrome(chrome_path, options=opt) # 크롬브라우저 실행
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
# 아이디 입력
id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython")
# 비밀번호 입력
pw = browser.find_element_by_css_selector("input#inputPwd")
pw.send_keys("q1w2e3!@#")
# 로그인 버튼 클릭
button = browser.find_element_by_css_selector("button#loginBtn")
button.click()
time.sleep(3) # 로그인 다 될 때까지 기다리기

# 이메일함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2) # 웹페이지 다 뜰때까지 기다리기

# 이메일 제목 크롤링
page_num = 2
while True:
    title = browser.find_elements_by_css_selector("strong.tit_subject")
    for i in title:
        print(i.text)
    # 다음 페이지로 이동
    try:
        next_button = browser.find_element_by_css_selector(f"span.paging_mail > a:nth-child({page_num+1})")
    except:
        print("======== 크롤링 끝! ===========")
        break
    next_button.click()
    time.sleep(1)
    page_num += 1

browser.close()
