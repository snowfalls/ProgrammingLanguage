import requests
from lxml import etree
import os
import time

# http://www.jj20.com/bz/zrfg/list_1_1.html
# http://www.jj20.com/bz/zrfg/list_1_2.html
# http://www.jj20.com/bz/zrfg/list_1_3.html
# http://www.jj20.com/bz/zrfg/list_1_4.html

num = 0 # 下载第几张图
for i in range(1, 94):
    # 1. 网页地址
    url = 'http://www.jj20.com/bz/zrfg/list_1_%s.html' % i

    # 2. 模拟发送请求
    time.sleep(0.5)
    response = requests.get(url)
    content = response.content.decode('gbk')

    # 3. 提取数据
    html = etree.HTML(content)
    url_list = html.xpath("//ul[@class='picbz']")

    # 最外层ul循环
    for ul in url_list:
        li_list = ul.xpath("./li")
        # li循环：获取图片网址和名字
        for li in li_list:
            # 获取图片名
            a_name = li.xpath("./a")[1]
            name = a_name.xpath('./text()')[0]
            # 获取图片地址
            imgs = li.xpath("./a")[0]
            img_src = imgs.xpath("./img/@src")[0] \
                if imgs.xpath("./img/@src") \
                else imgs.xpath("./img/@loadsrc")[0]
            print(name, img_src)

            # 保存图片
            time.sleep(0.5) # 睡眠0.5秒
            img_content = requests.get(img_src).content
            # 显示下载图片信息
            num += 1
            print("下载第%d张图片：名字[%s.png]" %(num, name))
            # 创建img文件夹，如果存在，就直接下载图片
            file_path = "./img"
            # 判断路径是否存在
            if os.path.exists(file_path):
                # 添加数据
                with open(file_path + "/%s.png" % name, 'wb') as f:
                    f.write(img_content)
            else:
                # 创建路径
                os.mkdir(file_path)
                # 添加数据
                with open(file_path + "%s.png" % name, 'wb') as f:
                    f.write(img_content)