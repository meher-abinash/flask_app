from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello, World!"

@app.route("/hello1")

def hello_world1():
    return "Hello, World1!"

@app.route("/hello2")

def hello_world2():
    return "Hello, World2!"

@app.route("/test")
def test():
    a = 5+6
    return "this is my first fun in flask {}".format(a)

@app.route("/input")
def request_input():
    data1 = request.args.get("x")
    return "this is my input from url {}".format(data1)


if __name__ == "__main__":
    app.run(host="0.0.0.0")