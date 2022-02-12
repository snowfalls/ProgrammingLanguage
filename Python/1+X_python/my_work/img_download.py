import requests
from lxml import etree
# 爬虫分为4步
# 1. 网页地址
url = "http://www.jituwang.com/tuku/201811/1046031.html"
# 2. 模拟浏览器发送请求
response = requests.get(url)
# UnicodeDecodeError: 'utf-8' codec can't 
# decode byte 0xce in position 305: invalid continuation byte
# print(response.content.decode("gbk"))
content = response.content.decode("gbk")
# 3. 规则提取
html = etree.HTML(content)
# 提取语法
res = html.xpath("//div[@class='viewMainPad']")[1]
# print(res)
# 提取属性,找图片名和下载地址
# 图片名
title = res.xpath("./img/@title")[0]
# 图片地址
img = res.xpath("./img/@src")[0]
print(title, img)
# 4.保存
# 下载图片
response = requests.get(img)
# 二进制图片 bits
# print(response.content)
img_content = response.content
file_path = "%s.png" % title
with open(file_path, "wb") as f:
    f.write(img_content)
    
