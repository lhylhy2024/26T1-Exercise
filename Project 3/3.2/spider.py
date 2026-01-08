import urllib.request
from bs4 import BeautifulSoup
import os


def spider(url):
    m = {}
    try:
        resp = urllib.request.urlopen("http://127.0.0.1:5000")
        html = resp.read().decode()
        soup = BeautifulSoup(html, "lxml")

        # 爬取电影名称
        div = soup.find("div", attrs={"class": "info"})
        m["mTitle"] = div.find("div", attrs={"class": "title"}).find("h3").text
        m["mNative"] = div.find("div", attrs={"class": "native"}).find("span", attrs={"class": "attrs"}).text
        m["mNickname"] = div.find("div", attrs={"class": "nickname"}).find("span", attrs={"class": "attrs"}).text
        # print(mTitle,",",mNative,",",mNickname)

        # 爬取导演与主演名字
        m["mDirectors"] = div.find("div", attrs={"class": "directors"}).find("span", attrs={"class": "attrs"}).text
        m["mActors"] = div.find("div", attrs={"class": "actors"}).find("span", attrs={"class": "attrs"}).text
        # print(mDirectors,",",mActors)

        # 爬取其他信息
        spans = div.find("div", attrs={"class": "others"}).find_all("span", attrs={"class": "attrs"})
        m["mTime"] = spans[0].text
        m["mCountry"] = spans[1].text
        m["mType"] = spans[2].text
        m["mComments"] = spans[3].text
        # print(mTitle,mCountry,mType,mComments)

        # 爬取电影图像
        src = soup.find("div", attrs={"class": "pic"}).find("img")["src"]
        # url = "http://127.0.0.1:5000/"
        src = urllib.request.urljoin(url, src)
        download(src)

    except Exception as err:
        print(err)
    return m


def download(src):
    try:
        p = src.rfind("/")
        name = src[p + 1:]
        print(name)
        resp = urllib.request.urlopen(src)
        data = resp.read()

        f = open("download\\" + name, "wb")
        print(f)
        f.write(data)
        print(f)
        f.close()
    except Exception as err:
        print(err)


def show(m):
    print("名称：", m["mTitle"])
    print("原名：", m["mNative"])
    print("别名：", m["mNickname"])
    print("导演：", m["mDirectors"])
    print("主演：", m["mActors"])
    print("时间：", m["mTime"])
    print("国家 ", m["mCountry"])
    print("类型：", m["mType"])
    print("评价：", m["mComments"])


if not os.path.exists("download"):
    os.mkdir("download")
m = spider("http://127.0.0.1:5000/")
show(m)
