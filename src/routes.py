from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html", the_title="Tiger Home Page")


@app.route("/symbol.html")
def symbol():
    return render_template("symbol.html", the_title="Tiger As Symbol")


@app.route("/myth.html")
def myth():
    return render_template("myth.html", the_title="Tiger in Myth and Legend")


if __name__ == "__main__":
    app.run(debug=True)
    print("done")
