import requests

# 反爬：阻止网络机器人爬取信息
url = "https://www.baidu.com/?tn=62095104_19_oem_dg"
# 反反爬：
# header反爬：User-Agent
# 将爬虫模拟成了浏览器
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
# 2.发起请求
response = requests.get(url,headers=header)
print(response.content.decode())