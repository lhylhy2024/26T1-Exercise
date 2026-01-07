import urllib.request
import re
import sqlite3


class MySpider:
    def openDB(self):
        """创建数据库和表"""
        self.con = sqlite3.connect("rates.db")
        self.cursor = self.con.cursor()

        # 删除已存在的表（如果存在）
        try:
            self.cursor.execute("DROP TABLE IF EXISTS rates")
        except Exception as err:
            print(f"Error while dropping table: {err}")

        # 创建新表
        sql = """CREATE TABLE rates \
                 ( \
                     Currency VARCHAR(256) PRIMARY KEY, \
                     TSP      REAL, \
                     CSP      REAL, \
                     TBP      REAL, \
                     CBP      REAL
                 )"""
        self.cursor.execute(sql)
        print("数据库表创建成功")

    def closeDB(self):
        """关闭数据库连接"""
        self.con.commit()
        self.con.close()
        print("数据库连接已关闭")

    def insertDB(self, Currency, TSP, CSP, TBP, CBP):
        """插入数据到数据库"""
        try:
            sql = "INSERT OR REPLACE INTO rates(Currency, TSP, CSP, TBP, CBP) VALUES(?, ?, ?, ?, ?)"
            self.cursor.execute(sql, [Currency, TSP, CSP, TBP, CBP])
            print(f"插入数据: {Currency}")
        except Exception as err:
            print(f"插入数据时出错 {Currency}: {err}")

    def show(self):
        """显示数据库中的数据"""
        print("\n=== 汇率数据表 ===")
        print("%-18s%-12s%-12s%-12s%-12s" % ("货币", "TSP", "CSP", "TBP", "CBP"))
        print("-" * 66)

        try:
            self.cursor.execute("SELECT Currency, TSP, CSP, TBP, CBP FROM rates ORDER BY Currency")
            rows = self.cursor.fetchall()

            if len(rows) == 0:
                print("数据库中没有数据")
                return

            for row in rows:
                print("%-18s%-12.2f%-12.2f%-12.2f%-12.2f" % (row[0], row[1], row[2], row[3], row[4]))
        except Exception as err:
            print(f"查询数据时出错: {err}")

    def spider(self, url):
        """爬取网页并解析数据"""
        print(f"正在访问: {url}")
        try:
            # 发送HTTP请求
            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            data = resp.read()
            html = data.decode('utf-8')

            print("网页获取成功，开始解析数据...")

            # 方法1: 使用正则表达式解析<tr>标签
            # 查找所有<tr>标签内容
            tr_pattern = r'<tr>(.*?)</tr>'
            tr_matches = re.findall(tr_pattern, html, re.DOTALL)

            print(f"找到 {len(tr_matches)} 个表格行")

            if len(tr_matches) == 0:
                print("未找到表格数据，尝试其他解析方法...")
                # 方法2: 直接查找<td>标签
                td_pattern = r'<td>(.*?)</td>'
                td_matches = re.findall(td_pattern, html)

                if len(td_matches) >= 6:
                    print(f"找到 {len(td_matches)} 个单元格")
                    # 每6个单元格为一组
                    for i in range(0, len(td_matches), 6):
                        if i + 5 < len(td_matches):
                            Currency = td_matches[i].strip()
                            unit = td_matches[i + 1].strip()

                            # 跳过标题行（如果包含"交易币"等字样）
                            if any(keyword in Currency for keyword in ["交易币", "Currency", "货币"]):
                                continue

                            try:
                                TSP = float(td_matches[i + 2].strip())
                                CSP = float(td_matches[i + 3].strip())
                                TBP = float(td_matches[i + 4].strip())
                                CBP = float(td_matches[i + 5].strip())

                                self.insertDB(Currency, TSP, CSP, TBP, CBP)
                            except ValueError as e:
                                print(f"转换数值失败 {Currency}: {e}")
                                continue
                else:
                    print("无法解析网页内容")
                    return
            else:
                # 处理每个<tr>标签
                for i, tr_content in enumerate(tr_matches):
                    # 在每个<tr>中查找所有<td>标签
                    td_pattern = r'<td>(.*?)</td>'
                    td_matches = re.findall(td_pattern, tr_content, re.DOTALL)

                    if len(td_matches) >= 6:
                        Currency = td_matches[0].strip()

                        # 跳过标题行
                        if any(keyword in Currency for keyword in ["交易币", "Currency", "货币"]):
                            continue

                        try:
                            # 注意：根据CSV文件结构，列顺序是：
                            # 0:交易币, 1:交易币单位, 2:现汇卖出价, 3:现钞卖出价, 4:现汇买入价, 5:现钞买入价
                            # 但是爬虫代码中的变量名可能需要调整
                            unit = td_matches[1].strip()
                            TSP = float(td_matches[2].strip())  # 现汇卖出价
                            CSP = float(td_matches[3].strip())  # 现钞卖出价
                            TBP = float(td_matches[4].strip())  # 现汇买入价
                            CBP = float(td_matches[5].strip())  # 现钞买入价

                            self.insertDB(Currency, TSP, CSP, TBP, CBP)
                        except ValueError as e:
                            print(f"转换数值失败 {Currency}: {e}")
                            continue

        except Exception as err:
            print(f"爬取过程中出错: {err}")

    def process(self):
        """主处理流程"""
        print("开始爬虫任务...")
        self.openDB()

        # 使用简单版本的路由，返回纯表格数据
        self.spider("http://127.0.0.1:5000/simple")

        # 或者使用完整页面版本
        # self.spider("http://127.0.0.1:5000/")

        self.show()
        self.closeDB()
        print("\n爬虫任务完成!")


# 主程序
if __name__ == "__main__":
    spider = MySpider()
    spider.process()