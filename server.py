from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_from_flask():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<name>")
def say_name(name):
    return "Hi " + name + "!"

@app.route("/repeat/<num>/hello")
def hello_repeat(num):
    return "hello " * int(num)

if __name__ == "__main__":
    app.run(debug = True)