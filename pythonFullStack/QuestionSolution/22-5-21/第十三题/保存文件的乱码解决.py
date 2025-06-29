import requests
import parsel
import csv
#生成1-19页的招聘信息列表
urls = [
    "http://www.52boro.com/mp-630/cat-21564/content_list/?sub_cat_id=&type_id=7920&keyword=&order_by=&cat_type=1&address_id=&page={}".format(
        i) for i in range(1, 20)]
#模拟 Chrome 浏览器请求，避免被网站识别为爬虫。
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
n = 1
for url_ in urls:
    resp = requests.get(url=url_, headers=headers).text
    # print(resp)
    #使用 CSS 选择器定位每个招聘信息卡片。
    select = parsel.Selector(resp)
    div_list = select.css('.content')
    #下面进行数据提取
    for div in div_list:
        title = div.css('div.weui-flex > div:nth-child(2) > div > div:nth-child(1) > div > div::text').get()
        time = div.css('.like-list::text').get()
        content = div.css('p a::text').get()
        with open('longxizhaoping.csv', mode='a', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([title, time, content])

    print(f'第{n}页在爬取中')
    n += 1
