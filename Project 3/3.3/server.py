import flask
app=flask.Flask(__name__,static_folder="images")

@app.route("/")
def index():
      return flask.render_template("movie.html")

@app.route("/<name>")
def show(name):
      if name.strip()=="":
            name="movie.html"
      print(name)
      return flask.render_template(name)

app.debug=True
app.run()