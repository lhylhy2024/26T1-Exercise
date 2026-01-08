import urllib.request
from bs4 import BeautifulSoup

class Queue:
      def __init__(self):
            self.st=[]
      def fetch(self):
            return self.st.pop(0)
      def enter(self,obj):
            self.st.append(obj)
      def empty(self):
            return len(self.st)==0

def spider(url):
      try:
            visited = []
            queue=Queue()
            queue.enter(url)
            visited.append(url)
            while not queue.empty():
                 url=queue.fetch()
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
                              queue.enter(url)
                              visited.append(url)
      except Exception as err:
            print(err)

spider("http://127.0.0.1:5000/")