import requests
from bs4 import BeautifulSoup
import json

url = 'https://baike.baidu.com/item/碳纤维/1492681?fr=aladdin'
headers = { 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res = requests.get(url,allow_redirects=False,headers=headers)
res.encoding = 'utf-8'
html = res.text
soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all(class_ = 'para')
'''res2 = res.json()
text2 = res2['para']'''
text= []
for i in items:
    text.append(i.text)
for i in text:
    print(i)
print(len(text))

with open(r'C:\Users\11038\Desktop\material mechanics small project\text.txt','w',encoding='utf-8') as file:
    for i in text:
        file.write(i)
        file.write('\n')
        