import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    """为爬虫提供结构化HTML数据"""
    try:
        f = open("rates.csv", "r", encoding="utf-8")
        rows = f.readlines()
        f.close()

        # 构建完整的HTML页面，包含完整的表格结构
        html = """<!DOCTYPE html>
<html>
<head>
    <title>汇率数据</title>
</head>
<body>
    <h1>银行汇率表</h1>
    <table border="1" cellpadding="5">
        <tr>
            <th>交易币</th>
            <th>交易币单位</th>
            <th>现汇卖出价</th>
            <th>现钞卖出价</th>
            <th>现汇买入价</th>
            <th>现钞买入价</th>
        </tr>"""

        # 处理每一行数据（跳过标题行）
        for i in range(1, len(rows)):
            row = rows[i].strip()
            if row:  # 确保不是空行
                cells = row.split(",")
                if len(cells) == 6:
                    html += "<tr>"
                    for cell in cells:
                        html += f"<td>{cell}</td>"
                    html += "</tr>"

        html += """
    </table>
</body>
</html>"""

        return html
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"


@app.route("/simple")
def simple_table():
    """简化的表格，只包含数据行（无表头），便于爬虫解析"""
    try:
        f = open("rates.csv", "r", encoding="utf-8")
        rows = f.readlines()
        f.close()

        html = ""
        # 跳过标题行，只输出数据行
        for i in range(1, len(rows)):
            row = rows[i].strip()
            if row:
                cells = row.split(",")
                if len(cells) == 6:
                    html += "<tr>"
                    for cell in cells:
                        html += f"<td>{cell}</td>"
                    html += "</tr>"

        return html
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)