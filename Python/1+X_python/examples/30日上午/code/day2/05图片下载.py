# 4
import requests
from lxml import etree
# 1.网页地址：
url = 'http://www.jituwang.com/tuku/201811/1046031.html'
# 2.m模拟浏览器发送请求
response = requests.get(url)
# 报错信息：'utf-8' codec can't decode byte 0xce in position 305: invalid continuation byte
# print(response.content.decode("gbk"))
content = response.content.decode("gbk")
# 3.规则提取
html = etree.HTML(content)
# div提取语法
res = html.xpath("//div[@class='viewMainPad']")[1]
# 找图片名和下载地址
# 图片名
title = res.xpath("./img/@title")[0]
# 图片地址
img = res.xpath("./img/@src")[0]
print(title,img)
# 4.保存
# 下载图片
response = requests.get(img)
# 二进制的图片 byte
# print(response.content)
img_content = response.content
# 文件名
file_path = "%s.png" % title
# 保存文件
with open(file_path,"wb") as f:
    f.write(img_content)


# 爬虫4步：

# 听课的老师：省份或城市，学校，名字