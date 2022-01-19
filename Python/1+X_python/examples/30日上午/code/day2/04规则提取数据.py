import requests
# 安装规则提取数据；第三方库：xpath
# pip install lxml
# etree:分析树
from lxml import etree
# 节点：
# 1.地址：
url = "https://www.baidu.com/?tn=62095104_19_oem_dg"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
# 2.发起请求
response = requests.get(url,headers=header)
# print(response.content.decode())
content = response.content.decode()
# 3.提取数据
# 将content的网页内容：使用分析树，转成节点格式
html = etree.HTML(content)
# 使用节点操作
#  1:// :全文搜索
#res = html.xpath("//div")
# 2:[@class]:属性
# res = html.xpath("//div[@class='s_tab']")
# res1 = html.xpath("//div[@id='s_tab']")

#3.  /：当前节点下一个节点
#4. 获取文字:text()
# 结束：全文找div,class属性是s-top-left s-isindex-wrap的div，
# 找这个div下面的a节点、
# 需要a节点下面的文字
# 5. 获取属性:@+属性名
# res = html.xpath("//div[@class='s-top-left s-isindex-wrap']/a/text()")
# res1 = html.xpath("//div[@class='s-top-left s-isindex-wrap']/a/@class")
# print(res)
# print(res1)
# 6.当前属性：'.'
res_list = html.xpath("//div[@class='s-top-left s-isindex-wrap']/a")
# print(res_list)
# 提取每个对象中的内容
for i in res_list:
    # print(i)
# 从当前节点开始
    txt = i.xpath("./text()")[0] # 当前a标签下的文字
    href = i.xpath("./@href")[0] # 当前a标签下的href属性
    print(txt,href,"sfsd")

# 6个节点操作
# //,/,.,[@name="a"],text(),@src





# 想要文字：text()
# 想要属性：@+属性名


