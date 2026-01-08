#爬取51游戏中任何游戏对应的搜索结果页面数据
import requests
import urllib

game_key = input("请输入游戏关键字：")

# 指定url
url = "https://game.51.com/search/action/game/"
params = {
    "q":game_key
}

# 发送请求
resp = requests.get(url,params)
# 获取响应数据
page_text = resp.text

# 持久化存储
file_name = '搜索关键字为' + game_key + '.html'
with open(file_name,'w',encoding='utf-8') as fp:
    fp.write(page_text)