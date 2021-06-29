import urllib.request as req
from bs4 import BeautifulSoup

your_champ = input("상대가 고른 챔프 입력 >> ")
headers = req.Request("https://www.op.gg/champion/statistics", headers={"Accept-Language":"ko-KR"})
code = req.urlopen(headers)
soup = BeautifulSoup(code, "html.parser")
champs = soup.select("div.champion-index__champion-item")
for i in champs:
    if i.attrs["data-champion-name"] == your_champ:
        a = i.select_one("a")
        url = "https://www.op.gg" + a.attrs["href"]
        url = req.urlopen(url).geturl()+"/matchup"
        headers = req.Request(url, headers={"Accept-Language":"ko-KR"})
        code = req.urlopen(headers)
        soup = BeautifulSoup(code, "html.parser")
        counter = soup.select("div.champion-matchup-list__champion > span:nth-child(2)")
        for i in counter:
            print(i.string)
