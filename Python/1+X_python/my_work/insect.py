#安装第三方库requests
# pip install request
# pip uninstall requests
# 安装规则提取数据第三方库： xpath
# pip install lxml
# etree:分析树
from lxml import etree
# 节点：
import requests
# 1.地址
url = "http://www.baidu.com"
url1 = "http://news.baidu.com"
url2 = "https://www.baidu.com/s?ie=UTF-8&wd=python"
# 反反爬：header反爬：User-Agent
# 将爬虫模拟成浏览器
header = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}



# 2.发起请求 enter键
response = requests.get(url,headers=header)
# print(response)
# <Response [200]> 对象 2--代表执行成功
#显示对象中的内容
# print(response.content.decode())
#content是二进制,字节类型
# print(response.text)
# text:中文
# 检查网页源码：爬虫获取内容

content = response.content.decode()
# print(content)
# 3.提取数据
# 将content的网页内容：使用分析树，转成节点格式
html = etree.HTML(content)
# 使用节点操作
# 1： // : 全文搜索
# 2：[class]属性
# res = html.xpath("//meta[@name='description']/@content")
# res1 = html.xpath("//div[@id='s_tab']")
# 3.文字
# 3. /：当前节点下一个节点
# 4. 文字：text()
# 全文找div，div的class属性是s-top-left s-isindex-wrap的div，
# 找这个div下面的a节点、需要a节点下面的文字
# 5.获取属性
# res = html.xpath("//div[@class='s-top-left s-isindex-wrap']/a/text()")
# res1 = html.xpath("//div[@class='s-top-left s-isindex-wrap']/a/@href")
# print(res)
# print(res1)
# 6.当前属性 .
res_list = html.xpath("//div[@class='s-top-left s-isindex-wrap']/a")
# print(res_list)
# 提取每个对象中的内容
for i in res_list:
    # print(i)
# 从当前属性节点开始
    txt = i.xpath("./text()")[0] #当前a标签下的文字
    href = i.xpath("./@href")[0] #当前a标签下的href属性
    print(txt, href)

# 6个节点操作
# //全局搜索， /当前节点的子节点， .当前节点开始, [@name='a'], text(), @src

