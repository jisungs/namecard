from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/username/<name>")
def greet(name):
    return f"<h1> Hello your name is{name}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)