import requests
from lxml import etree
import sys,io
from bs4 import BeautifulSoup
# for i in range(0,251,25):
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
url='https://movie.douban.com/top250?start=0&filter='
headers={'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
resp=requests.get(url,headers=headers)
#print(resp.text)
# e=etree.HTML(resp.text)
#
# infos=e.xpath('//div[@class="bd"]/p[1]/text()')
# for info in infos:
#
#     info=info.replace('\n','').replace('...','').replace('/','').strip()
#
#     print(info)

bs=BeautifulSoup(resp.text,'lxml')
lst=bs.find_all('div',class_='bd')

for item in lst:
    alst=item.find_all('p')
    for  a in alst:
        print(a.text.split(' '))
        print('----------------------------------')
