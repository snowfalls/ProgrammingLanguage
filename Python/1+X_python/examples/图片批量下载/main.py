import requests
from lxml import etree
import os # 系统操作，不需要安装
import time
#娟娟壁纸
# 1. url
# url = 'http://www.jj20.com/bz/zrfg/'
# # 2. 发起请求
# # request
# response = requests.get(url)
# # gbk中文解码
# content = response.content.decode('gbk')
# # 3. 提取数据
# html = etree.HTML(content)
# ul_list = html.xpath("//ul[@class='picbz']")
# print(ul_list)
# 最外ul循环

num = 0
for i in range(1,94):
    url = "http://www.jj20.com/bz/zrfg/list_1_%s.html" % i
    for ul in ul_list:
        # print(ul)
        li_list = ul.xpath("./li")
        # li循环，获取图片地址和名字
        for li in li_list:
            # print(li)
            # 获取图片名
            a_name = li.xpath("./a")[1]
            name = a_name.xpath("./text()")[0]
            # print(name)
            # 图片链接地址
            imgs = li.xpath("./a")[0]
            # loadsrc 
            img_src = imgs.xpath("./img/@src")[0] \
                if imgs.xpath("./img/@src") else imgs.xpath("./img/@loadsrc")[0]
            # print(name, img_src)

            # 保存
            # 将图片内容取出
            img_con = requests.get(img_src).content

            # 创建img文件夹，如果存在直接下载，否则创建新文件夹
            file_path = "./图片批量下载/img"
            # 判断路径是否存在，返回结果是True或False
            if os.path.exists(file_path):
                pass
            else:
                # 创建文件夹
                os.mkdir(file_path)
                # 添加数据
            
            path = file_path+"/%s.png" % name
            print(path)
            with open(path, "wb") as f:
                f.write(img_con)

