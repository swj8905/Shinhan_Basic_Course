from bs4 import BeautifulSoup
import urllib.request as req

while True:
    print("===== 국가 선택 =====")
    print("1. 미국")
    print("2. 일본")
    print("3. 유럽")
    print("4. 중국")
    print("5. 종료")
    print("=====================")
    menu = int(input("선택 >> "))
    if menu == 5:
        break
    unit = ["달러", "엔", "유로", "위안"]
    user_input = int(input(f"금액 입력(단위 : {unit[menu-1]}) >> "))
    if menu == 2:
        user_input /= 100
    code = req.urlopen("https://finance.naver.com/marketindex/")
    soup = BeautifulSoup(code, "html.parser")
    price = soup.select("ul#exchangeList span.value")
    result = float(price[menu-1].string.replace(",","")) * user_input
    print(f"환전 결과 : {result:.2f} 원")