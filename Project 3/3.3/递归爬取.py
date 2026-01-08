import urllib.request
from bs4 import BeautifulSoup

def spider(url):
      global visited
      try:
            #print(url)
            #input()
            visited.append(url)
            resp = urllib.request.urlopen(url)
            html = resp.read().decode()
            soup = BeautifulSoup(html, "lxml")
            div = soup.find("div", attrs={"class": "info"})
            if div:
                  mTitle = div.find("div", attrs={"class": "title"}).find("h3").text
                  print("---",mTitle)
            else:
                  div = soup.find("div", attrs={"id": "country"})
                  print(div.text)
            links = soup.find_all("a")
            for link in links:
                   href=urllib.parse.quote(link["href"])
                   url=urllib.request.urljoin(url,href)
                   if not url in visited:
                         spider(url)
      except Exception as err:
            print(err)

visited=[]
spider("http://127.0.0.1:5000/")