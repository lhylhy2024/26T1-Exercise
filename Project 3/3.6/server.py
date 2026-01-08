import flask

app = flask.Flask(__name__, static_folder="images")


@app.route("/")
def show():
    pageRowCount = 5
    # 获取页面索引
    if "pageIndex" in flask.request.values:
        pageIndex = int(flask.request.values.get("pageIndex"))
    else:
        pageIndex = 1
    # 计算分页参数
    startRow = (pageIndex - 1) * pageRowCount
    endRow = pageIndex * pageRowCount
    movies = []
    try:
        # 读取电影数据
        fobj = open("movies.csv", "r", encoding="utf-8")
        rows = fobj.readlines()
        count = 0
        for row in rows:
            if row.strip("\n").strip() != "":
                count += 1
        # 排除标题行
        count = count - 1
        # 计算总页数
        pageCount = count // pageRowCount
        if count % pageRowCount != 0:
            pageCount += 1

        # 提取当前页的电影数据
        rowIndex = 0
        # 1开始遍历，跳过标题行
        for i in range(1, count + 1):
            row = rows[i]
            # 检查当前行索引是否在分页的范围内
            if rowIndex >= startRow and rowIndex < endRow:
                row = row.strip("\n")
                # 使用split(",")将行数据分割成列表
                s = row.split(",")
                m = {}
                m["ID"] = s[0]
                m["mImage"] = s[0] + s[1]
                m["mTitle"] = s[2]
                movies.append(m)
            rowIndex += 1
        fobj.close()
    except Exception as err:
        print(err)
    return flask.render_template("movie.html", movies=movies, pageIndex=pageIndex, pageCount=pageCount)


app.run()