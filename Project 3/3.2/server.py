import flask
app = flask.Flask(__name__,static_folder="images")
@app.route("/")
def index():
    # 渲染并返回模板页面
    return flask.render_template("movie_xiao.html")

app.debug = True
app.run()