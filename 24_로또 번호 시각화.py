from bs4 import BeautifulSoup
import urllib.request as req
from collections import Counter
import matplotlib.pyplot as plt

code = req.urlopen("https://signalfire85.tistory.com/28")
soup = BeautifulSoup(code, "html.parser")
number = soup.select("td.xl69 > span")
result = []
for i in number:
    print(i.string)
    result.append(int(i.string))

count_result = Counter(result)
count_result = sorted(count_result.items())
print(count_result)
x = []
y = []
for i in count_result:
    x.append(i[0])
    y.append(i[1])

plt.bar(x, y, tick_label=x)
plt.show()
