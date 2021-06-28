from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

keyword = input("키워드 입력 >> ")
encoded = par.quote(keyword) # 한글 --> 특수한 문자열
page_num = 1
while True:
    code = req.urlopen(f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord={encoded}&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord={encoded}&KeyLastWord={encoded}&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={page_num}")
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("a.bo3 > b")
    price = soup.select("tr > td:nth-child(1) > a.bo_used > b")
    if len(title) == 0:
        break
    for i in range(len(title)):
        try:
            print(title[i].string, price[i].string)
        except:
            print(title[i].string, "-")
    page_num += 1