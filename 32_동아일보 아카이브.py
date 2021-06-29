from bs4 import BeautifulSoup
import requests

sess = requests.session()
h = {"Referer": "https://secure.donga.com/membership/login.php?gourl=https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19870629%26mode%3D19870629%2F0001484119%2F1"}
post_data = {
"gourl": "https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19870629%26mode%3D19870629%2F0001484119%2F1",
"bid": "talingpython",
"bpw": "xkfdldvkdlTjs2"
}
result = sess.post("https://secure.donga.com/membership/trans_exe.php", data=post_data, headers=h)
# print(result.text)

# 크롤링
code = sess.get("https://www.donga.com/archive/newslibrary/view?idx=19870629%2F0001484124%2F1")
soup = BeautifulSoup(code.text, "html.parser")
content = soup.select_one("div.article_txt")
print(content.text)
