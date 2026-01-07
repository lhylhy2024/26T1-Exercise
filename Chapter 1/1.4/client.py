import urllib.parse
import urllib.request

try:
    s = input("输入要查询的外汇：")
    value = urllib.parse.quote(s)
    html = urllib.request.urlopen("http://127.0.0.1:5000?currency="+value)
    html = html.read()
    html = html.decode()
    print(html)
    
except Exception as err:
    print(err)