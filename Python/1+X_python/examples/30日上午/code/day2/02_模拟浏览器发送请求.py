
#安装第三方库requests
# pip install requests:安装
# pip uninstall requests:卸载
import requests
# 1.地址：
url = "https://www.baidu.com/?tn=62095104_19_oem_dg"
# url1 = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&fenlei=256&rsv_pq=9dc7951a00039601&rsv_t=96a0XJobAseSCdbn9%2FjmBuLCuKCMCScqV4elQ9sGa8aO%2BNap03l4eKb6Npw&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=3&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=936&rsv_sug4=1580"

# 2.发起请求
response = requests.get(url)
# <Response [200]> 对象
print(response) # 成功
# 显示对象中的内容
# content:字节类型
print(response.content.decode())
# text；中文
# print(response.text)

# 检查网页源码：爬虫获取的内容