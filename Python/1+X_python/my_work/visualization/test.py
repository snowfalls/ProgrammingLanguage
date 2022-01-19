# 爬虫获取数据生成json，然后用json绘图
import requests
from lxml import etree
import os
import json
# 1. 地址
url = "http://www.weather.com.cn/weather/101270101.shtml"
# 2. 发起请求
response = requests.get(url)
content = response.content.decode()
# 3. 提取数据
html = etree.HTML(content)
# 提取日期和温度
li_list = html.xpath("//ul[@class='t clearfix']/li")
weather_list = []
# 循环提取日期
for li in li_list:
    item = {}
    date = li.xpath("./h1/text()")[0]
    # print(date)
    max_tem = li.xpath("./p[@class='tem']/span/text()")[0]
    # print(max_tem)[0]
    min_tem = li.xpath("./p[@class='tem']/i/text()")[0]
    item["min_tem"] = int(min_tem.replace("℃",""))
    item["max_tem"] = int(max_tem)
    item["date"] =  date
    weather_list.append(item)

# 4.保存
with open("weather.json", "w", encoding="utf-8") as f:
    # ensure_ascii:允许中文
    # indent：首行缩减
    json.dump(weather_list,f,ensure_ascii=False,indent=2)

print("文件保存成功")

