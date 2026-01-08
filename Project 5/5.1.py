#东方财富首页数据爬取
import requests

# 指定url
url = "https://www.eastmoney.com/"

# 发请求
resp = requests.get(url)
resp.encoding = 'utf-8'

# 获取字符串形式的响应数据
page_text = resp.text
print(page_text)

with open("./caifu.html",'w',encoding="utf-8") as fp:
    fp.write(page_text)
