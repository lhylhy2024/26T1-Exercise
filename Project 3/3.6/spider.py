import urllib.request
from bs4 import BeautifulSoup

def myFilter(tag):
     if tag.name=="a" and tag.text=="下一页":
            return True
     return False

def spider(url):
      global count
      try:
           print(url)
           resp=urllib.request.urlopen(url)
           html=resp.read().decode()
           soup=BeautifulSoup(html,"lxml")
           lis=soup.find("ul").find_all("li")
           for li in lis:
                   div=li.find("div",attrs={"class":"info"})
                   mTitle=li.find("div",attrs={"class":"title"}).find("h3").text
                   count+=1
                   print(count,mTitle)
           #查找翻页按钮
           link=soup.find("div",attrs={"class":"paging"}).find(myFilter)
           href=link["href"].strip()
           if href!="#":
                  url=urllib.request.urljoin(url,href)
                  spider(url)
      except Exception as err:
           print(err)
count=0
spider("http://127.0.0.1:5000")