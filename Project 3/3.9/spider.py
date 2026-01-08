import requests
from bs4 import BeautifulSoup
import openpyxl

def html_get():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    global lst
    lst = [['编号', '名称', '推荐语', '评分', '链接地址']]  # 初始化为一个包含标题行的列表
    for i in range(10):  # 产生0-9的整数序列
        url = f'https://movie.douban.com/top250?start={i * 25}&filter='  # 通过循环改变url地址，实现多页查询
        resp = requests.get(url, headers=header)  # 请求方式为GET
        bs = BeautifulSoup(resp.text, 'html.parser')  # 解析的内容，解析器
        grid_view = bs.find('ol', class_='grid_view')  # 标签，类样式
        all_li = grid_view.find_all('li')
        for item in all_li:  # 遍历所有li
            no = item.find('em').text  # 电影序号
            title = item.find('span', class_='title').text  # 标题
            inq1 = item.find('span', class_='inq')  # 推荐语
            if inq1:
                inq = inq1.text
            else:
                inq = "无推荐语"  # 如果没有推荐语，设置默认值
            rat = item.find('span', class_='rating_num').text  # 评分
            url_films = item.find('a')['href']  # 标签，属性
            print(no, title, inq, rat, url_films)
            lst.append([no, title, inq, rat, url_films])  # 添加进列表

def file_storage():
    wb = openpyxl.Workbook()  # 新建一个工作簿
    sheet = wb.active  # 建一个工作表
    sheet.title = 'filmsTop250'  # 工作表的标题
    for item in lst:  # 将数据导入工作表
        sheet.append(item)
    wb.save('films.xlsx')  # 文件名

if __name__ == '__main__':
    html_get()
    file_storage()